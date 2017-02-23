from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addCourse$', views.addCourse),
    url(r'^destroy/(?P<id>\d+)/$', views.destroy, name="remove_url"),
    url(r'^remove/(?P<id>\d+)/$', views.remove, name="delete")
]
