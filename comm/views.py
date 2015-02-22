from reportlab.pdfgen import canvas

from django.http import HttpResponse, HttpResponseForbidden
from django.utils import timezone
from django.utils.encoding import force_unicode
from django.template import RequestContext, loader

from comm.models import CommunionDay

def generate_report(request, communion_day_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    
    
    communion_day = CommunionDay.objects.get(id=communion_day_id)

    filename = '%s %s' % (force_unicode(communion_day.name),
            timezone.now().date())

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = \
            'attachment; filename="%s.pdf"' % filename

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    
    return response
