# productores/views.py
from django.shortcuts import render, redirect
from .models import Productor, Finca, Vivero
from .forms import ProductorForm, FincaForm, ViveroForm

# Gestión de Fincas
def listar_fincas(request):
    fincas = Finca.objects.all()
    return render(request, 'productores/listar_fincas.html', {'fincas': fincas})

def registrar_finca(request):
    if request.method == 'POST':
        form = FincaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fincas')
    else:
        form = FincaForm()
    return render(request, 'productores/registrar_finca.html', {'form': form})

def editar_finca(request, pk):
    finca = Finca.objects.get(pk=pk)
    if request.method == 'POST':
        form = FincaForm(request.POST, instance=finca)
        if form.is_valid():
            form.save()
            return redirect('listar_fincas')
    else:
        form = FincaForm(instance=finca)
    return render(request, 'productores/editar_finca.html', {'form': form, 'finca': finca})

def eliminar_finca(request, pk):
    finca = Finca.objects.get(pk=pk)
    finca.delete()
    return redirect('listar_fincas')

# Gestión de Viveros
def listar_viveros(request):
    viveros = Vivero.objects.all()
    return render(request, 'productores/listar_viveros.html', {'viveros': viveros})

def registrar_vivero(request):
    if request.method == 'POST':
        form = ViveroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_viveros')
    else:
        form = ViveroForm()
    return render(request, 'productores/registrar_vivero.html', {'form': form})

def editar_vivero(request, pk):
    vivero = Vivero.objects.get(pk=pk)
    if request.method == 'POST':
        form = ViveroForm(request.POST, instance=vivero)
        if form.is_valid():
            form.save()
            return redirect('listar_viveros')
    else:
        form = ViveroForm(instance=vivero)
    return render(request, 'productores/editar_vivero.html', {'form': form, 'vivero': vivero})

def eliminar_vivero(request, pk):
    vivero = Vivero.objects.get(pk=pk)
    vivero.delete()
    return redirect('listar_viveros')

# productores/views.py
from .models import Labor
from .forms import LaborForm

def listar_labores(request):
    labores = Labor.objects.all()
    return render(request, 'productores/listar_labores.html', {'labores': labores})

def registrar_labor(request):
    if request.method == 'POST':
        form = LaborForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_labores')
    else:
        form = LaborForm()
    return render(request, 'productores/registrar_labor.html', {'form': form})

def editar_labor(request, pk):
    labor = Labor.objects.get(pk=pk)
    if request.method == 'POST':
        form = LaborForm(request.POST, instance=labor)
        if form.is_valid():
            form.save()
            return redirect('listar_labores')
    else:
        form = LaborForm(instance=labor)
    return render(request, 'productores/editar_labor.html', {'form': form, 'labor': labor})

def eliminar_labor(request, pk):
    labor = Labor.objects.get(pk=pk)
    labor.delete()
    return redirect('listar_labores')
