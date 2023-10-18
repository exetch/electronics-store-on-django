from django.db import models


NULLABLE = {'null': True, 'blank': True}
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение (превью)", **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за покупку")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    version_number = models.CharField(max_length=50, verbose_name="Номер версии")
    version_name = models.CharField(max_length=255, verbose_name="Название версии")
    is_active = models.BooleanField(default=False, verbose_name="Текущая версия")

    def __str__(self):
        return f"{self.product} - Версия {self.version_number}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
