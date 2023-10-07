from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contact
class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'latest_products'
    ordering = ['date_created']
    paginate_by = 5


class ContactListView(ListView):
    model = Contact
    template_name = 'catalog/contact.html'
    context_object_name = 'contacts'

class ContactSubmitView(View):
    template_name = 'catalog/success.html'

    def post(self, request):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        # Данные из формы получены
        print(f"Имя: {name}")
        print(f"Телефон: {phone}")
        print(f"Сообщение: {message}")
        return render(request, self.template_name)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'