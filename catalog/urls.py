from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    path('success/', views.ContactSubmitView.as_view(), name='contact_submit'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]