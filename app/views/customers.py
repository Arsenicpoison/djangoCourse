from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Customer
from app.forms import CustomerForm

def index(request):
    assert isinstance(request, HttpRequest)
    customers = Customer.objects.all()
    return render(
        request,
        'app/customers/index.html',
        {
            'customers': customers
        }
    )
    
def add(request):
    form = CustomerForm()
    return render(
        request, 
        'app/customers/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Customer has been saved successfully !")
        return redirect('/customers')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
            customers = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customers)
        return render(
            request,
            'app/customers/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = customerForm(request.POST)
        else:
            customers = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=customers)
        if form.is_valid():
            form.save()
        messages.success(request, "Customer has been updated successfully !")
        return redirect('/customers')
    
def delete(request, id):
    customer = Customer.objects.get(pk=id)
    customer.delete()
    messages.success(request, "Customer has been removed successfully !")
    return redirect('/customers')