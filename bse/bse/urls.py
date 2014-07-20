from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'task.views.index'),
    url(r'^import_db/$', 'task.views.import_db'),
    url(r'^stockdata/$', 'task.views.stockdata'),
    url(r'^goc/(?P<code>.*)/(?P<day>\d{2})(?P<month>\d{2})(?P<year>\d{4})/$', 'task.views.getdata'),
    url(r'^goc_range/(?P<c>.*)/(?P<day>\d{2})(?P<month>\d{2})(?P<year>\d{4})/(?P<d>\d{2})(?P<m>\d{2})(?P<y>\d{4})/$', \
    	'task.views.getdatabetweentwodate'),

    url(r'^admin/', include(admin.site.urls)),
)
