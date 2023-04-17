from django.http import HttpResponse
from django.template import loader

from .mappings import get_all_products


# Create your views here.

def dashboard(request):
    products = get_all_products()

    template = loader.get_template('dashboard.html')

    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))
