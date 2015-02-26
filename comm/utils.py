from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from django.forms.util import flatatt

def make_html_link(href, name, method='GET', extra_attrs=None):
    if method == 'GET':
        attrs = {'href': href}
    elif method == 'POST':
        attrs = {'data-post-url': href, 'href': '#'}
    if not extra_attrs:
        extra_attrs = {}
    attrs.update(extra_attrs)
    return mark_safe(u'<a %s>%s</a>' % (flatatt(attrs),
                     conditional_escape(force_unicode(name))))
