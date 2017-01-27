from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new/$', views.create_view, name='create_view'),
    url(r'^(?P<lb_pk>[0-9]+)/edit/$',
        views.edit_view, name='edit_view'),
    url(r'^(?P<lb_pk>[0-9]+)/opening_hours/new/$',
        views.add_opening_hours, name='add_opening_hours'),
    url(r'^(?P<oh_pk>[0-9]+)/opening_hours/remove/$',
        views.remove_opening_hours, name='remove_opening_hours'),
]
