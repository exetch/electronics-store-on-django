from django.core.cache import cache
from catalog.models import Category


def get_cached_categories():

    categories = cache.get('categories_list')

    if categories is None:
        categories = Category.objects.all()
        cache.set('categories_list', categories, 30)
        print("Данные загружены из БД.")

    else:
        print("Данные загружены из кэша. Я молодец.")

    return categories