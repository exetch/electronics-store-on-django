from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/create/', views.BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/update/<slug:slug>/', views.BlogPostUpdateView.as_view(), name='blog_post_update'),
    path('blog/delete/<slug:slug>/', views.BlogPostDeleteView.as_view(), name='blog_post_delete'),
    path('blog/<slug:slug>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
]