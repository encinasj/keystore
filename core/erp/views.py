#Django
from django.shortcuts import render
from django.views.generic import ListView
from django.utils.decorators import method_decorator

#ours
from core.erp.models import Category


def frontpage(request):
    template_name = 'base.html'
    return render(request, template_name)

def client(request):
    template_name = 'client.html'
    return render ( request, template_name)


class CategoryList(ListView):
    #show category list
    model = Category
    template_name = 'category.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorías'
        
        return context

def product(request):
    template_name = 'product.html'
    return render ( request, template_name)