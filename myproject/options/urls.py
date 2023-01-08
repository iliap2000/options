from django.urls import path

from . import views

urlpatterns = [
    path('options/', views.options_view, name='options'),
    path('pricing/', views.pricing, name='pricing'),
    path('', views.options_view, name='options'),
]
