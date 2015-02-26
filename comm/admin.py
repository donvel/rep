# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.admin.helpers import InlineAdminFormSet, InlineAdminForm
from django.utils.functional import curry
from django.core.urlresolvers import reverse

from comm.models import CommunionDay, Branch, Diocese, Report, \
        CustomTextConfig, CustomText, Service, Attendance
from comm.utils import make_html_link


class AttendanceAdmin(admin.ModelAdmin):
    def get_inline_formsets(self, request, formsets, inline_instances,
                        obj=None):
        inline_admin_formsets = []
        for inline, formset in zip(inline_instances, formsets):
            fieldsets = list(inline.get_fieldsets(request, obj))
            readonly = list(inline.get_readonly_fields(request, obj))
            prepopulated = dict(inline.get_prepopulated_fields(request, obj))
            inline_admin_formset = AttendanceInlineAdminFormSet(inline, formset,
                fieldsets, prepopulated, readonly, model_admin=self)
            inline_admin_formsets.append(inline_admin_formset)
        return inline_admin_formsets


class AttendanceInlineAdminFormSet(admin.helpers.InlineAdminFormSet):

    def help_text(self):
        if self.formset.dioceses:
            return u""
        else:
            return u'Kliknij "Zapisz i kontynuuj edycję", ' + \
                    u'aby móc edytować listę obecności.'

    def table_iter(self):
        inline_dict = {}
        counter = 0
        for iform in self:
            s = iform.form.initial.get('service')
            d = iform.form.initial.get('diocese')
            inline_dict[(s,d)] = iform, counter
            counter += 1
        return [([inline_dict[(s.id, d.id)] for s in self.formset.services], d)
                for d in self.formset.dioceses]


def attendance_formset_factory(FormSet, initial=None, services=None,
        dioceses=None):
    class AttendanceFormSet(FormSet):
        def __init__(self, *args, **kwargs):
            old_initial = kwargs.pop('initial', [])
            new_initial = old_initial + initial if initial else []
            super(AttendanceFormSet, self).__init__(*args,
                    **dict(kwargs, initial=initial))
            self.services = services
            self.dioceses = dioceses
    return AttendanceFormSet


class AttendanceInline(admin.TabularInline):
    model = Attendance
    template = 'comm/attendance_table.html'
    can_delete = False

    def _get_services(self, obj):
        return Service.objects.all()

    def _get_dioceses(self, obj):
        if not obj:
            return Diocese.objects.none()
        return Diocese.objects.filter(branch=obj.branch)

    def _get_filled(self, obj):
        if not obj:
            return Attendance.objects.none()
        return Attendance.objects.filter(report=obj)
    
    def get_extra(self, request, obj=None, **kwargs):
        sc = self._get_services(obj).count()
        dc = self._get_dioceses(obj).count()
        fc = self._get_filled(obj).count()
        return sc * dc - fc

    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        services = self._get_services(obj)
        dioceses = self._get_dioceses(obj)
        filled = set((at.service.id, at.diocese.id)
                for at in self._get_filled(obj))
        if request.method == "GET":
            for s in services:
                for d in dioceses:
                    if (s.id, d.id) not in filled:
                        initial += [{'service': s.id, 'diocese': d.id}]
        
        FormSet = super(AttendanceInline, self) \
                .get_formset(request, obj, **kwargs)
        
        return attendance_formset_factory(FormSet, 
                initial=initial, services=services, dioceses=dioceses)


class CustomTextInline(admin.StackedInline):
    model = CustomText
    extra = 1
    
    def _get_unfilled(self, obj):
        always_present = CustomTextConfig.objects.filter(obligatory=True)
        if obj is None:
            return always_present
        return always_present.exclude(customtext__report=obj)

    def get_extra(self, request, obj=None, **kwargs):
        return self._get_unfilled(obj).count() + 1

    def get_formset(self, request, obj=None, **kwargs):
        initial = []
        if request.method == "GET":
            unfilled = self._get_unfilled(obj)
            initial = [{'config': c.id} for c in unfilled]

        formset = super(CustomTextInline, self) \
                .get_formset(request, obj, **kwargs)
        formset.__init__ = curry(formset.__init__, initial=initial)
        return formset


class ReportAdmin(AttendanceAdmin):
    fields = ['communion_day', 'branch', 'file_report']
    inlines = [AttendanceInline, CustomTextInline]

    class Media:
        css = {'all': ('css/comm/attendance_admin.css',)}


class ReportInline(admin.StackedInline):
    model = Report
    readonly_fields = ['edit_link']
    fields = ['branch', 'edit_link']
    extra = 0

    def edit_link(self, instance):
        if instance.id is not None:
            return make_html_link(reverse('admin:comm_report_change',
                args=(instance.id,)), u"przejdź do edycji sprawozdania")
        return u"zapisz, aby przejść do edycji"
    edit_link.short_description = u"Edycja"


class CommunionDayAdmin(admin.ModelAdmin):
    inlines = [ReportInline,]
    readonly_fields = ['generate_link']
    fields = ['name', 'topic', 'date', 'handout', 'generate_link']
    
    def generate_link(self, instance):
        if instance.id is not None:
            return make_html_link(reverse('comm.views.generate_report',
                args=(instance.id,)), u"generuj raport")
        return ""
    generate_link.short_description = u"Zbiorczy raport"


class DioceseInline(admin.TabularInline):
    model = Diocese
    extra = 0


class BranchAdmin(admin.ModelAdmin):
    inlines = [DioceseInline,]


admin.site.unregister(Group)
admin.site.register(CommunionDay, CommunionDayAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Diocese)
admin.site.register(CustomTextConfig)
admin.site.register(Service)

