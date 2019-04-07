from CMSApp import views
from django.conf.urls import url

app_name = 'CMSApp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^input/$', views.input, name='input'),
    url(r'^detail/(?P<report_pk>\w+)/$', views.detail, name='detail'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^something/$', views.somethingnew),
    url(r'^manage_data/$', views.manage_public, name='manage'),
    url(r'^manage_data/add/$', views.add_public, name='add_public'),
    url(r'^manage_data/del/(?P<civ_pk>\w+)/$', views.del_public, name='delete_public')
]