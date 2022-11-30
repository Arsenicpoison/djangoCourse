from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Order
from app.forms import OrdersForm

def index(request):
    assert isinstance(request, HttpRequest)
    orders = Order.objects.all()
    return render(
        request,
        'app/orders/index.html',
        {
            'orders': orders
        }
    )
    
def add(request):
    form = OrdersForm()
    return render(
        request, 
        'app/orders/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "orders has been saved successfully !")
        return redirect('/orders')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
            orders = Orders.objects.get(pk=id)
            form = OrdersForm(instance=customers)
        return render(
            request,
            'app/orders/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = OrdersForm(request.POST)
        else:
            orders = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
        messages.success(request, "Orders has been updated successfully !")
        return redirect('/orders')
    
def delete(request, id):
    orders = Orders.objects.get(pk=id)
    orders.delete()
    messages.success(request, "Customer has been removed successfully !")
    return redirect('/orders')

def getProducts(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id = category_id).order_by('product_name')
    return render(
        request,
        'app/orders/getProducts.html',
        {
            'products': products
        }
    )
    
def getUnitPrice(request):
    id_product = request.GET.get('id_product')
    product = Product.objects.get(pk = id_product)
    return render(
        request,
        'app/orders/getUnitPrice.html',
        {
            'product': product
        }
    )