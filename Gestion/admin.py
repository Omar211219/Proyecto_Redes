from django.contrib import admin
from Gestion.models import Comentario, Suscripcion, Cita, Pregunta

# Register your models here.

class ComentarioAdmin(admin.ModelAdmin):
    list_display=("nombre", "correo", "asunto", "fecha")
    search_fields=("nombre", "correo")
    list_filter=("fecha",)
    date_hierarchy="fecha"

class SuscripcionAdmin(admin.ModelAdmin):
    list_display=("correo", "fecha")
    search_fields=("correo",)
    list_filter=("fecha",)
    date_hierarchy="fecha"

class CitaAdmin(admin.ModelAdmin):
    list_display=("reservacion","nombre", "correo", "telefono", "fecha", "terminada")
    search_fields=("reservacion","nombre", "correo", "telefono")
    list_filter=("reservacion", "fecha", "terminada",)
    date_hierarchy="fecha"

class PreguntaAdmin(admin.ModelAdmin):
    list_display=("pregunta",)
    search_fields=("pregunta",)

admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Suscripcion, SuscripcionAdmin)
admin.site.register(Cita, CitaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)