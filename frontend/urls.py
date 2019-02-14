from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('main', views.main),
    path('detail/<str:name>', views.detail)
]