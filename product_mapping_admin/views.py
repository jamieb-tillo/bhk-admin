from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .mappings import get_all_products
from .forms.add import AddForm


# Create your views here.

def dashboard(request):
    products = get_all_products()

    template = loader.get_template('dashboard.html')

    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))

def add(request):
    
    if request.method == 'GET':
        form = AddForm()

    else:
        form = AddForm(request.POST)
        return HttpResponse({'content': form.cleaned_data})

    return render(request, 'add.html', {"form": form})
