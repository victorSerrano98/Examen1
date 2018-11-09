from django.shortcuts import render, redirect
from app.modelo.models import Estudiante
from .forms import FormularioEstudiante
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def Principal(request):
    listaUsuarios = Estudiante.objects.all().order_by('apellidos')
    context = {
        'lista' : listaUsuarios
    }
    return render(request, 'estudiante/principal_estudiante.html', context)

def crear(request):
    formulario = FormularioEstudiante(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante = Estudiante()
            estudiante.cedula = datos.get('cedula')
            estudiante.matricula = datos.get('matricula')
            estudiante.nombres = datos.get('nombres')
            estudiante.apellidos = datos.get('apellidos')
            estudiante.genero = datos.get('genero')
            estudiante.carrera = datos.get('carrera')
            estudiante.save()
            return redirect(Principal)

    context = {
        'f': formulario,
        'mensaje': 'hola',
    }
    return render(request, 'estudiante/crear_esudiante.html', context)
def modificar(request):
    dni = request.GET['cedula']
    estudiante = Estudiante.objects.get(cedula = dni)
    formulario = FormularioEstudiante(request.POST, instance=estudiante)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante.cedula = datos.get('cedula')
            estudiante.nombres = datos.get('nombres')
            estudiante.apellidos = datos.get('apellidos')
            estudiante.genero = datos.get('genero')
            estudiante.estado = datos.get('estado')
            estudiante.correo = datos.get('correo')
            estudiante.telefono = datos.get('telefono')
            estudiante.celular = datos.get('celular')
            estudiante.direccion = datos.get('direccion')
            estudiante.save()
            return redirect(Principal)
    else:
        formulario = FormularioEstudiante(instance=estudiante)

    context = {
        'f': formulario,
    }
    return render(request, 'estudiante/crear_esudiante.html', context)
