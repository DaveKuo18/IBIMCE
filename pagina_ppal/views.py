from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import reuniones_comunes, reuniones_especiales

# Create your views here.

def index(request):
    return render(request, "ibim/index.html", {
        "comunes": reuniones_comunes.objects.all(),
        "especiales": reuniones_especiales.objects.all()
    })

def predicaciones(request):
    return render(request, "ibim/predicaciones.html")

def todas_las_predicaciones(request, anio):
    return render(request, f"cuatrimestres/{anio}.html")

def formulario(request):
    return render(request, "ibim/form.html")

def enviar_form(request):
    if request.method == "POST":
        asunto = "Nuevo contacto de la página: " + request.POST["nombre"]
        mensaje = "Mensaje enviado por " + request.POST["nombre"] + ", email " + request.POST["mail"] + ", numero " + request.POST["numero"] + ". Mensaje: " + request.POST["mensaje"]
        email_from = settings.EMAIL_HOST_USER
        recipient = ["ibimciudadevita@gmail.com"]
        send_mail(asunto, mensaje, email_from, recipient)
        return render(request, "ibim/mensaje_enviado.html")
    
    return render(request, "ibim/formulario.html")

def cielo(request):
    return render(request, "ibim/cielo.html")

def sobre_nosotros(request):
    return render(request, "ibim/sobre_nosotros.html")