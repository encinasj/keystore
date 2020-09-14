from django.shortcuts import render
from core.erp.models import Category

def frontpage(request):
    template_name = 'base.html'
    return render(request, template_name)

def client(request):
    template_name = 'client.html'
    return render ( request, template_name)

def category(request):
    template_name = 'category.html'
    category = Category.objects.all()
    context = {
        'category': category,
        }
    return render(request, template_name, context)

def product(request):
    template_name = 'product.html'
    return render ( request, template_name)