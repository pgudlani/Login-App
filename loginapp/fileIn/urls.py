from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from fileIn.views import *

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view()),
    url(r'^signup/$', SignUpView.as_view()),
    url(r'^home/$', HomeView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^upload/$', UploadView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
