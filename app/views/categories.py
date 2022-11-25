from django.http import HttpRequest
from django.shortcuts import render,redirect
from app.models import Category
from app.forms import categoryForm

def index (request):
    assert isinstance(request,HttpRequest)
    categories = Category.objects.all()
    return render(request, 
                  'app/categories/index.html',
                  {
                    'categories': categories
                  }
                )
def add(request):
        return render(request, 'app/categories/add.html')
def store(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valide():
            form.save()
        return redirect('/categories')
    

def edit (request,id):
    assert isinstance(request, 
                      'app/categories/index.html'
                      )
    if request.method == "GET":
        if id == 0:
            form = categoryForm()
        else:
            category = category.objects.get(pk =id)
            form = categoryForm(instance = category)
        return render(
            request,
            'app/categories/edit.html',
            {
                'form':form
            }
        )
    else:
        if id ==0:
            form = categoryForm(request.POST)
        else:
            category = category.objects.get(pk =id)
            form = categoryForm(request,POST,instance = category)
        if form.is_valide():
            form.save()
        return redirect ('/categories')
    
def delete (request,id):
    category = category.objects.get(pk =id)
    category.detele()
    return redirect ('/categories')
    
        