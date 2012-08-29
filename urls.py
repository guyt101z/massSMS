from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # admin urls
    #premade send action
    url(r'^admin/sendpremade/(?P<ids>.+)$', 'massSMS.userupload.admin_views.sendpremade'),
    # SMS send admin action
    url(r'^admin/sendsms/submit/$', 'massSMS.userupload.admin_views.sendsms_submit'),
    # SMS send admin dialog (asks for message, confirms selected users, etc.)
    url(r'^admin/sendsms/(?P<ids>.+)$', 'massSMS.userupload.admin_views.sendsms_dialog'),
    # general admin url
    url(r'^admin/', include(admin.site.urls)),

    # non-admin urls
    url(r'^/?(.*)$', 'massSMS.userupload.user_views.home'),

)
