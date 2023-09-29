from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contacts/', views.contact_view, name='contacts'),
    path('success/', views.contact_submit_view, name='contact_submit'),
]