from django.db import models
from django.urls import reverse
from django.core.mail import send_mail

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.CharField(max_length=200, verbose_name="Slug", null=True, blank=True)
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog_previews/', verbose_name="Превью (изображение)")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[str(self.slug)])

    def increment_views(self):
        self.views += 1
        self.save()
        if self.views == 100:
            subject = 'Поздравляем! Ваша статья достигла 100 просмотров'
            message = f'Статья "{self.title}" достигла 100 просмотров. Поздравляем!'
            from_email = 'alexeyb494@gmail.com'
            recipient_list = ['gassemark@gmail.com']
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
