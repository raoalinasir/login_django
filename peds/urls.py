from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('^read/$', views.read_mail, name='read_mail'),
    re_path('^compose/$', views.compose, name='compose'),
    re_path('^profile/$', views.profile, name='profile')
]