from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Product
from django.contrib import messages
from hanif import urls
from .forms import AddTableForm


def dashboard(request):
    products = Product.objects.all()
    table = Paginator(products, 8)
    table_list = request.GET.get('table')
    table = table.get_page(table_list)

    return render(request, 'dashboard.html', {
        'table': table,
    })

def dashboard_table(request, pk):
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('table', pk)
    page_list = paginator.get_page(page_number)

    return render(request, 'table.html', {
        'page_list': page_list,
    })

def table_list(request, pk):
    if request.user.is_authenticated:
        # Look Up Tables
        table_list = Product.objects.get(id=pk)
        form = AddTableForm(request.POST or None, instance=table_list)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, 'table_list.html', {
            'table_list': table_list,
            'form': form,
        })
    else:
        messages.error(request, 'You Must Be Logged In To View This Page...')
        return redirect('dashboard')

def delete_table(request, pk):
    if request.user.is_authenticated:
        delete_it = get_object_or_404(Product, id=pk)
        delete_it.delete()
        messages.success(request, 'Table List Deleted Successfully...')
        return redirect('dashboard')
    else:
        messages.error(request, 'You Must Be Logged In To Do This Action...')
        return redirect('dashboard')

def add_table(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddTableForm(request.POST or None)
            if form.is_valid():
                add_tables = form.save()
                return redirect('dashboard')
        else:
            form = AddTableForm()
        return render(request, 'add_table.html', {'form': form})
    else:
        messages.error(request, 'You Must Be Logged In To Do This Action...')
        return redirect('dashboard')