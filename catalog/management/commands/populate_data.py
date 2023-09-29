from django.core.management.base import BaseCommand
from catalog.models import Category
import json

class Command(BaseCommand):
    help = 'Заполняет базу данных категориями'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        with open('category_fixture.json', 'r', encoding='utf-8') as json_file:
            categories_data = json.load(json_file)
            categories_to_create = []
            for category_data in categories_data:
                category = Category(
                    name=category_data['fields']['name'],
                    description=category_data['fields']['description']
                )
                categories_to_create.append(category)
            Category.objects.bulk_create(categories_to_create)