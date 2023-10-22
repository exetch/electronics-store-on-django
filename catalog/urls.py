from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    path('success/', views.ContactSubmitView.as_view(), name='contact_submit'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('product/<int:product_id>/create_version/', views.CreateVersionView.as_view(), name='create_version'),
    path('product/<int:product_id>/choose_active_version/', views.ChooseActiveVersionView.as_view(), name='choose_active_version'),
    path('authentication-required/', views.authentication_required_page, name='authentication_required_page'),
]