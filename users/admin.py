from django.contrib import admin

from users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'email_verificated', 'phone_number')
    search_fields = ('first_name', 'email')
