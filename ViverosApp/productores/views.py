# productores/views.py
from django.shortcuts import render, redirect
from .models import Productor
from .forms import ProductorForm

def listar_productores(request):
    productores = Productor.objects.all()
    return render(request, 'productores/listar.html', {'productores': productores})

def registrar_productor(request):
    if request.method == 'POST':
        form = ProductorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productores')
    else:
        form = ProductorForm()
    return render(request, 'productores/registrar.html', {'form': form})

def editar_productor(request, pk):
    productor = Productor.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductorForm(request.POST, instance=productor)
        if form.is_valid():
            form.save()
            return redirect('listar_productores')
    else:
        form = ProductorForm(instance=productor)
    return render(request, 'productores/editar.html', {'form': form, 'productor': productor})

def eliminar_productor(request, pk):
    productor = Productor.objects.get(pk=pk)
    productor.delete()
    return redirect('listar_productores')
