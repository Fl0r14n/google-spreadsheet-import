from django.conf.urls import patterns, include, url
from django.contrib import admin
import social_auth.urls
from web import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'google_spreadsheet_import.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(social_auth.urls)),
    url(r'^$', views.home, name='index'),
)
