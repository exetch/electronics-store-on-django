from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'is_published', 'views')
    list_filter = ('is_published', 'date_created')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.site_header = 'Администрирование блога'

