from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^base/', views.base, name='base'),
    url(r'^$', views.index, name='index'),
]