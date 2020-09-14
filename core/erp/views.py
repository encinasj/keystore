from django.shortcuts import render

def frontpage(request):
    template_name = 'base.html'
    return render(request, template_name)

def client(request):
    template_name = 'client.html'
    return render ( request, template_name)

def product(request):
    template_name = 'product.html'
    return render ( request, template_name)