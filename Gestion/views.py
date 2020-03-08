from django.shortcuts import render
from django.template import Template
from django.shortcuts import render
from Gestion.models import Comentario, Suscripcion, Cita, Pregunta

# Create your views here.

import datetime
import re

def inicio(request):
    
    if request.method=='POST':
        comentario=Comentario()
        suscripcion=Suscripcion()

        if 'correo' in request.POST:
            suscripcion.correo=request.POST['correo']
            suscripcion.fecha=datetime.datetime.now()
            if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', suscripcion.correo.lower()):
              suscripcion.save()
        
        else:
            comentario.nombre=request.POST['name']
            comentario.correo=request.POST['email']
            comentario.asunto=request.POST['subject']
            comentario.mensaje=request.POST['message']
            comentario.fecha=datetime.datetime.now()
            comentario.save()
        

    return render(request, "inicio.html")

def reservacion(request):

    if request.method=='POST':
        suscripcion=Suscripcion()
        suscripcion.correo=request.POST['correo']
        suscripcion.fecha=datetime.datetime.now()
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', suscripcion.correo.lower()):
            suscripcion.save()

    return render(request, "reservacion.html")

def cita(request,service):

    if request.method=='POST':
        cita=Cita()
        suscripcion=Suscripcion()

        if 'correo' in request.POST:
            suscripcion.correo=request.POST['correo']
            suscripcion.fecha=datetime.datetime.now()
            if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', suscripcion.correo.lower()):
              suscripcion.save()
        
        else:
            cita.nombre=request.POST['name']
            cita.correo=request.POST['email']
            cita.telefono=request.POST['tel']
            cita.fecha=request.POST['date']
            cita.mensaje=request.POST['message']
            
            if service==1:
                cita.reservacion="Servicio de Emergencia"
            if service==2:
                cita.reservacion="Vacunas"
            if service==3:
                cita.reservacion="Cirujía"
            if service==4:
                cita.reservacion="Exámenes de Control"
            if service==5:
                cita.reservacion="Micro Chips"
            if service==6:
                cita.reservacion="Pensión"
            if service==7:
                cita.reservacion="Asistencia Dental"
            if service==8:
                cita.reservacion="Aseo"
            if service==9:
                cita.reservacion="Estilista"
            
            fecha=datetime.datetime.now()
            fecha_actual=fecha.strftime('%Y-%m-%d')
            if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', cita.correo.lower()) and str(fecha_actual) <= str(cita.fecha):
                cita.save()

    return render(request, "cita.html", {"service":service})

def politica(request):

    if request.method=='POST':
        suscripcion=Suscripcion()
        suscripcion.correo=request.POST['correo']
        suscripcion.fecha=datetime.datetime.now()
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', suscripcion.correo.lower()):
            suscripcion.save() 
    
    return render(request, "politica de privacidad.html")

def pregunta(request):

    if request.method=='POST':
        suscripcion=Suscripcion()
        suscripcion.correo=request.POST['correo']
        suscripcion.fecha=datetime.datetime.now()
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', suscripcion.correo.lower()):
            suscripcion.save()

    return render(request, "pregunta.html")

def respuesta(request):

    if request.GET["pregunta"]:
        pregunta=request.GET["pregunta"]
        respuestas=Pregunta.objects.filter(pregunta__icontains=pregunta)
        return render(request, "respuesta.html", {"respuestas":respuestas, "query":pregunta})