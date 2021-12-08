from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect

from .forms import demandsForm, demandsItemForm
from .models import demands , demandsItem
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_demands(request, id_client):
    template_name = 'demands/add_demands.html'
    context = {}
    if request.method == 'POST':
        form = demandsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.client = Client.objects.get(id=id_client)
            f.save()
            form.save_m2m()
            return redirect('demands:list_demands')
    form = demandsForm()
    context['form'] = form
    return render(request, template_name, context)

def list_demands(request):
    template_name = 'demands/list_demands.html'
    demands = demands.objects.filter()
    demands_items = demandsItem.objects.filter()
    products = Product.objects.filter()
    clients = Client.objects.filter()
    context = {
        'demands': demands,
        'demands_items': demands_items,
        'products': products,
        'clients': clients
    }
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def delete_demands(request, id_demands):
    demands = demands.objects.get(id=id_demands)
    demands.delete()
    return redirect('demands:list_demands')
@login_required(login_url='/contas/login/')
def add_demands_item(request, id_demands):
    template_name = 'demands/add_demands_item.html'
    context = {}
    if request.method == 'POST':
        form = demandsItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.demands = demands.objects.get(id=id_demands)
            f.save()
            form.save_m2m()
            return redirect('demands:list_demands')
    form = demandsItemForm()
    context['form'] = form
    return render(request, template_name, context)
    
@login_required(login_url='/contas/login/')
def delete_demands_item(request, id_demands_item):
    demandsitem = demandsItem.objects.get(id=id_demands_item)
    demandsitem.delete()
    return redirect('demands:list_demands')

@login_required(login_url='/contas/login/')
def edit_demands_status(request, id_demands):
    template_name = 'demands/edit_demands_status.html'
    context ={}
    demands = get_object_or_404(demands, id=id_demands)
    if request.method == 'POST':
        form = demandsForm(request.POST, instance=demands)
        if form.is_valid():
            form.save()
            return redirect('demands:list_demands')
    form = demandsForm(instance=demands)
    context['form'] = form
    return render(request, template_name, context)
