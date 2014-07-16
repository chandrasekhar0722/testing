from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^import_db/$', 'csvtask.views.import_db'),
    url(r'^stockdata/$', 'csvtask.views.stockdata'),
    #url(r'^goc/(?P<tag>.*)/(\d+)/(\d{2})/(\d{4})/$', 'csvtask.result.getdata'),
    #url(r'^goc/(?P<companyname>.*)/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/$', 'csvtask.result.getdata'),
    url(r'^goc/(?P<companyname>.*)/(?P<day>\d{2})(?P<month>\d{2})(?P<year>\d{4})/$', 'csvtask.result.getdata'),
    url(r'^goc/(?P<c>.*)/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/(?P<d>\d{2})/(?P<m>\d{2})/(?P<y>\d{4})/$', 'csvtask.result2.getdatabetweentwodate'),
    
    # url(r'^testing/', include('testing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
