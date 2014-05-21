from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from employer.views import *

urlpatterns = patterns('',
    url(r'^signup/$', SignUpView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
