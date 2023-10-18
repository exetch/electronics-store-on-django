from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import ProductForm, VersionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Product, Contact, Version

class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'latest_products'
    ordering = ['date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['latest_products']:
            active_version = Version.objects.filter(product=product, is_active=True).last()
            product.active_version = active_version
        return context



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

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    def get_success_url(self):
        return reverse_lazy('product_detail', args=[self.object.pk])

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', args=[self.object.pk])

    def post(self, request, *args, **kwargs):
        if "add_version" in request.POST:
            product_id = self.kwargs['pk']
            return redirect('create_version', product_id=product_id)
        else:
            return super().post(request, *args, **kwargs)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')

class CreateVersionView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'

    def get_form_kwargs(self):
        form_kwargs = super(CreateVersionView, self).get_form_kwargs()
        product = get_object_or_404(Product, pk=self.kwargs['product_id'])
        form_kwargs['instance'] = Version(product=product)
        return form_kwargs

    def get_success_url(self):
        return reverse_lazy('choose_active_version', args=[self.kwargs['product_id']])


class ChooseActiveVersionView(View):
    template_name = 'catalog/choose_active_version.html'

    def get(self, request, product_id):
        versions = Version.objects.filter(product_id=product_id)
        return render(request, self.template_name, {'versions': versions})

    def post(self, request, product_id):
        active_version_id = request.POST.get('active_version')
        product_versions = Version.objects.filter(product_id=product_id)

        for version in product_versions:
            if str(version.id) == active_version_id:
                version.is_active = True
            else:
                version.is_active = False
            version.save()

        return redirect('home')