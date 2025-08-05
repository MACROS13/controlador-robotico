from django import forms
from .models import Robot, Sensor, Tarea

class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = ['nombre', 'descripcion']

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['robot', 'tipo', 'descripcion']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['robot', 'nombre', 'descripcion']

class BuscarRobotForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, label="Buscar por nombre")
