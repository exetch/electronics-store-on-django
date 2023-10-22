from django.http import HttpResponseRedirect
from django.urls import reverse
import re
class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            path = request.path

            if path.startswith('/product/') and not is_product_url(path):
                return HttpResponseRedirect(reverse('authentication_required_page'))

            if path.startswith('/category/'):
                return HttpResponseRedirect(reverse('authentication_required_page'))

        return self.get_response(request)
def is_product_url(path):
    return re.match(r'^/product/\d+/', path)