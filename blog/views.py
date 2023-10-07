from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy
from django.utils.text import slugify


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by('-date_created')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.increment_views()
        return super().get(request, *args, **kwargs)


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blog/blog_post_form.html'
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog_post_list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.cleaned_data['title'])
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blog/blog_post_form.html'
    fields = ['title', 'slug', 'content', 'preview', 'is_published']
    context_object_name = 'blog_post'


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blog_post_confirm_delete.html'
    context_object_name = 'blog_post'
    success_url = reverse_lazy('blog_post_list')
