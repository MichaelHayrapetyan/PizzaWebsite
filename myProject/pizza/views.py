from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza
from .forms import PizzaForm
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Company


def pizza_list(request):
    if request.method == 'POST':
        search_query = request.GET.get('search_query')
        pizzas = Pizza.objects.filter(pizza_type__icontains=search_query)
    else:
        search_query = ''
        pizzas = Pizza.objects.all()
    return render(request, 'pizza/pizza_list.html', {'pizzas': pizzas, 'search_query': search_query})


def add_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pizza:pizza_list')
    else:
        form = PizzaForm()
    return render(request, 'pizza/add_pizza.html', {'form': form})


def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    return render(request, 'pizza/PizzaDetailView.html', {'pizza': pizza})


def update_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect('pizza:pizza_list')
    else:
        form = PizzaForm(instance=pizza)
    return render(request, 'pizza/update_pizza.html', {'form': form, 'pizza': pizza})


def delete_pizza(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    if request.method == 'POST':
        pizza.delete()
        return redirect('pizza:pizza_list')
    return render(request, 'pizza/delete_pizza.html', {'pizza': pizza})

