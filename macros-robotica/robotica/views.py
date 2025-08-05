from django.shortcuts import render, redirect
from .models import Robot
from .forms import RobotForm, SensorForm, TareaForm, BuscarRobotForm

def index(request):
    return render(request, 'index.html')

def crear_robot(request):
    if request.method == 'POST':
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RobotForm()
    return render(request, 'crear_robot.html', {'form': form})

def crear_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SensorForm()
    return render(request, 'crear_sensor.html', {'form': form})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})

def buscar_robot(request):
    form = BuscarRobotForm(request.GET or None)
    robots = None
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            robots = Robot.objects.filter(nombre__icontains=nombre)
        else:
            robots = Robot.objects.all()
    return render(request, 'buscar_robot.html', {'form': form, 'robots': robots})
