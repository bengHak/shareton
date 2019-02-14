from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('main/', views.main),
    path('detail/<str:name>', views.detail),
    path('payment/<str:name>/<str:time>/<str:price>/', views.payment),
    path('payment_done/',views.payment_done)
]