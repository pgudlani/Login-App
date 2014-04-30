from django.conf.urls import patterns, include, url

from fileIn.views import LoginView

urlpatterns = patterns('',
    url(r'^login$', LoginView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
