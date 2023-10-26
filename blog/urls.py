from django.urls import path
from django.views.decorators.cache import never_cache

from . import views

urlpatterns = [
    path('blog/', views.BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/create/', never_cache(views.BlogPostCreateView.as_view()), name='blog_post_create'),
    path('blog/update/<slug:slug>/', never_cache(views.BlogPostUpdateView.as_view()), name='blog_post_update'),
    path('blog/delete/<slug:slug>/', never_cache(views.BlogPostDeleteView.as_view()), name='blog_post_delete'),
    path('blog/<slug:slug>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
]