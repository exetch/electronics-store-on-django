from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Contact
def home_view(request):
    latest_products = Product.objects.order_by('date_created')[:5]
    for product in latest_products:
        print(f"Product Name: {product.name}, Price: {product.purchase_price}")
    context = {'latest_products': latest_products}
    return render(request, 'catalog/home.html', context)

def contact_view(request):
    contacts = Contact.objects.all()
    return render(request, 'catalog/contact.html', {'contacts': contacts})

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


from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})