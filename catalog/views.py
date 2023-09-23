from django.shortcuts import render

def home_view(request):
    # отображение домашней страницы
    return render(request, 'catalog/home.html')

def contact_view(request):
    # отображение страницы с контактной информацией
    return render(request, 'catalog/contact.html')