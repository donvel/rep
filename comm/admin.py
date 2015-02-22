import urllib

from django.contrib import admin
from django.contrib.admin.helpers import InlineAdminFormSet, InlineAdminForm
from django.utils.functional import curry
from django.core.urlresolvers import reverse

from comm.models import CommunionDay, Branch, Diocese, Report, \
        CustomTextConfig, CustomText, Service, Attendance
        #Conclusion
from comm.utils import make_html_link

"""
class ConclusionInline(admin.TabularInline):
    model = Conclusion
    extra = 2
"""
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
    """def __iter__(self):
        if not hasattr(self.formset, 'dioceses'):
            self.regular_iter()
        else:
            inline_dict = {}
            for iform in self.regular_iter():
                s = iform.form.initial.get('service')
                d = iform.form.initial.get('diocese')
                inline_dict[(s,d)] = iform
            print inline_dict
            for d in self.formset.dioceses:
                for s in self.formset.services:
                    yield inline_dict[(s.id, d.id)]
            yield inline_dict[(None, None)]
    def __iter__(self):
        return self.regular_iter()
    """


    def table_iter(self):
        inline_dict = {}
        counter = 0
        for iform in self:
            s = iform.form.initial.get('service')
            d = iform.form.initial.get('diocese')
            print 's, d = ', s, d
            inline_dict[(s,d)] = iform, counter
            counter += 1
        print inline_dict.keys()
        return (((inline_dict[(s.id, d.id)] for s in self.formset.services), d)
                for d in self.formset.dioceses)
    

    def __iter__(self):
        for form, original in zip(self.formset.initial_forms,
                self.formset.get_queryset()):
            view_on_site_url = self.opts.get_view_on_site_url(original)
            yield InlineAdminForm(self.formset, form, self.fieldsets,
                self.prepopulated_fields, original, self.readonly_fields,
                model_admin=self.opts, view_on_site_url=view_on_site_url)
        for form in self.formset.extra_forms:
            yield InlineAdminForm(self.formset, form, self.fieldsets,
                self.prepopulated_fields, None, self.readonly_fields,
                model_admin=self.opts)
        yield InlineAdminForm(self.formset, self.formset.empty_form,
            self.fieldsets, self.prepopulated_fields, None,
            self.readonly_fields, model_admin=self.opts)

class CustomTextInline(admin.StackedInline):
    model = CustomText
    extra = 1
    
    def _get_unfilled(self, obj):
        always_present = CustomTextConfig.objects.filter(obligatory=True)
        if obj is None: # mozliwe ??
            return always_present
        else:
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


def attendance_formset_factory(FormSet, initial=None, services=None, dioceses=None):
    class AttendanceFormSet(FormSet):
        def __init__(self, *args, **kwargs):
            old_initial = kwargs.pop('initial', [])
            new_initial = old_initial + (initial if initial else [])
            super(AttendanceFormSet, self).__init__(*args,
                    **dict(kwargs, initial=new_initial))
            print 'now initial = ', self.initial #Ech...
            # self.initial = initial
            self.services = services
            self.dioceses = dioceses
    return AttendanceFormSet



class AttendanceInline(admin.TabularInline):
    model = Attendance
    fields = ['number']
    extra = 0
    template = 'comm/attendance_table.html'
    can_delete = False

    def _get_services(self, obj):
        return Service.objects.all()

    def _get_dioceses(self, obj):
        if obj is None:
            assert False # mozliwe ?
        return Diocese.objects.filter(branch=obj.branch)

    def _get_filled(self, obj):
        if obj is None:
            assert False # mozliwe ?
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

        print 'initial: ', initial, ' filled: ', filled
        
        FormSet = super(AttendanceInline, self) \
                .get_formset(request, obj, **kwargs)
        
        return attendance_formset_factory(FormSet, 
                initial=initial, services=services, dioceses=dioceses)

class ReportAdmin(AttendanceAdmin):
    inlines = [CustomTextInline, AttendanceInline]# ConclusionInline,]


class ReportInline(admin.StackedInline):
    model = Report
    extra = 0


class CommunionDayAdmin(admin.ModelAdmin):
    inlines = [ReportInline,]
    readonly_fields = ['generate_link']
    fields = ['name', 'topic', 'date', 'handout', 'generate_link']
    
    def generate_link(self, instance):
        if instance.id is not None:
            return make_html_link(reverse('comm.views.generate_report',
                args=(instance.id,)), "generuj raport")
        return None
    generate_link.short_description = u"Zbiorczy raport"

class DioceseInline(admin.TabularInline):
    model = Diocese
    extra = 0

class BranchAdmin(admin.ModelAdmin):
    inlines = [DioceseInline,]


admin.site.register(CommunionDay, CommunionDayAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Diocese)
admin.site.register(CustomTextConfig)
admin.site.register(Service)
admin.site.register(Attendance)

