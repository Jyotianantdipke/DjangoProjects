from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def add_product(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='InventoryManagement/addproduct.html'
    context={'form':form}
    return render(request,template_name, context)

@login_required(login_url='login')
def show_product(request):
    records=Product.objects.all()
    template_name='InventoryManagement/showproduct.html'
    context={'records':records}
    return render(request,template_name,context)


def update_product(request,id):
    record=Product.objects.get(id=id)
    form=ProductForm(instance=record)
    if request.method=='POST':
        form=ProductForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name='InventoryManagement/addproduct.html'
    context={'form':form}
    return render(request, template_name, context)

def delete_product(request,id):
    record=Product.objects.get(id=id)
    record.delete()
    return redirect('show')


def home_view(request):
    template_name='InventoryManagement/home.html'
    context={}
    return render(request, template_name, context)