# project wide urls
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse
from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm
admin.autodiscover()


# import your urls from each app here, as needed
#import matcher.urls

urlpatterns = patterns('',

    # urls specific to this app
   (r'^accounts/password_change/done/$', 
        'django.contrib.auth.views.password_change_done'),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^matcher/', include('matcher.urls')),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # catch all, redirect to matcher home view
    url(r'^', RedirectView.as_view(url='/matcher/home')),
     

)
