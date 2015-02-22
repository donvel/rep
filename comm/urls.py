from django.conf.urls import patterns, url

from comm import views

urlpatterns = patterns('',
    # ex: /comm/3/generate/
    url(r'^(?P<communion_day_id>\d+)/generate/$', views.generate_report,
        name='generate'),
)
