from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .mappings import *
from .forms.add import AddForm
from .forms.edit import EditForm


# Create your views here.

def success(request, request_type):
    return render(request, 'success.html', {'type': request_type})


def dashboard(request):
    products = get_all_products()

    template = loader.get_template('dashboard.html')

    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))


def add(request):

    if request.method == 'POST':

        form = AddForm(request.POST)

        data = {
            'product_id': form.data['product_id'],
            'brand': form.data['brand'],
            'delivery_method': form.data['delivery_method']
        }

        response = create_new_product(data)

        if response.status_code == 201 or response.status_code == 200:
            return success(request, 'created')

    else:
        form = AddForm()

    return render(request, 'add.html', {'form': form})


def edit(request):

    data = request.POST

    form = EditForm(initial={
        'product_id': data['product_id'],
        'brand': data['brand'],
        'delivery_method': data['delivery_method']

    })

    return render(request, 'edit.html', {'form': form})


def submit(request):

    form = EditForm(request.POST)

    data = {
        'brand': form.data['brand'],
        'delivery_method': form.data['delivery_method']
    }

    product_id = form.data['product_id']

    response = edit_product_mapping(product_id, data)

    if response.status_code == 200:
        return success(request, 'updated')


def delete(request):

    product_id = request.POST['product_id']

    response = delete_product_mapping(product_id)

    if (response.status_code == 200):
        return success(request, 'deleted')
