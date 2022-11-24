from django.http import HttpRequest
from django.shortcuts import render
from app.models import category
from app.forms import categoryForm



def edit (request,id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id ==0:
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
def delete(request,id):
    category = category.objects.get(pk =id)
    category.detele()
    return redirect ('/categories')
    
        