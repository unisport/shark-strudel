from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.localbusiness_index, name='localbusiness_index'),
]
