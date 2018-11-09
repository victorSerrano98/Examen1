from django.contrib import admin

from .models import Estudiante

class AdminEstudiante(admin.ModelAdmin):
    list_display = ["cedula", "matricula", "apellidos", "nombres","carrera", "genero"]
    list_editable = ["apellidos", "nombres"]
    search_fields = ["cedula"]

    class Meta:
        model = Estudiante

admin.site.register(Estudiante, AdminEstudiante)