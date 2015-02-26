# -*- coding: UTF-8 -*-

from wkhtmltopdf.views import PDFTemplateResponse

from django.http import HttpResponse, HttpResponseForbidden
from django.utils import timezone
from django.utils.encoding import force_unicode
from django.template import RequestContext, loader
from django.conf import settings

from comm.models import CommunionDay, Service, Diocese, Branch, Attendance, \
        CustomTextConfig, CustomText, Report


def _generate_cday_report(cday):
    
    def generate_head():
        head = {}
        head['name'] = cday.name
        head['date'] = cday.date
        head['topic'] = cday.topic
        return head

    def generate_attendance():
        att = {}
        att['title'] = u"Lita obecności"
        rows = []
        
        services = Service.objects.all()
        attendances = Attendance.objects.filter(report__communion_day=cday)
        first_row = [u""] + [s.short_name for s in services] + [u"Suma"]
        rows += [first_row]

        for branch in Branch.objects.all():
            row = [branch.name]
            branch_atts = attendances.filter(diocese__branch=branch)
            
            number_sum = 0
            for service in services:
                atts = branch_atts.filter(service=service)
                number = sum(att.number for att in atts)
                row += [number]
                number_sum += number
            row += [number_sum]

            rows += [row]
    
        att['rows'] = rows
        return att

    def generate_text_fields():
        fields = []
        return fields

    def generate_text_mfields():
        mfields = []
        reports = Report.objects.filter(communion_day=cday)
        for config in CustomTextConfig.objects.all():
            if not config.use_in_report:
                continue
            mfield = {}
            mfield['title'] = config.name
            parts = []
            custom_texts = CustomText.objects.filter(config=config)

            for report in reports:
                part = {}
                part['title'] = unicode(report.branch)
                body = u""
                
                try:
                    text = custom_texts.get(report=report)
                    body = text.content
                except CustomText.DoesNotExist:
                    pass

                if not body:
                    continue
                part['body'] = body
                parts += [part]

            if len(parts) == 0:
                continue
            mfield['parts'] = parts
            mfields += [mfield]
        return mfields
    
    report = {}
    report['head'] = generate_head()
    report['attendance'] = generate_attendance()
    report['text_fields'] = generate_text_fields()
    report['text_multifields'] = generate_text_mfields()
    report['css_path'] = 'file://%scss/comm/report.css' % settings.STATIC_ROOT

    return report


def generate_report(request, communion_day_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    
    
    communion_day = CommunionDay.objects.get(id=communion_day_id)

    template = loader.get_template('comm/report.html')
    
    context = RequestContext(request, {'report': 
        _generate_cday_report(communion_day)})
    
    filename = '%s %s' % (force_unicode(communion_day.name),
            timezone.now().date())

    response = PDFTemplateResponse(request, template, context=context,
            filename=filename)
    #response = HttpResponse(template.render(context))

    """

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = \
            'attachment; filename="%s.pdf"' % filename
    """

    
    return response
