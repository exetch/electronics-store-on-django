from django.shortcuts import render
def home_view(request):
    # отображение домашней страницы
    return render(request, 'catalog/home.html')

def contact_view(request):
    # отображение страницы с контактной информацией
    return render(request, 'catalog/contact.html')

def contact_submit_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        # Данные из формы получены
        print(f"Имя: {name}")
        print(f"Телефон: {phone}")
        print(f"Сообщение: {message}")
        return render(request, 'catalog/success.html')

    return render(request, 'contacts.html')