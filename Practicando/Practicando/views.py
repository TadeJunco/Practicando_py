from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from Tade.models import curso

def saludo(request):
	return HttpResponse("Hola arrancando con el proyecto!")
def dia_de_hoy (request):
	dia = datetime.now()
	return HttpResponse(f"Hoy es día:<br>{dia}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a el proyecto de Tade")


def probando_template(request):

    nombre = "Tadeo"
    apellido = "Junco"
    diccionario = {"nombre": nombre, "apellido": apellido, "notas": [4, 8, 9, 10, 7, 8]}
    mi_html = open('./Practicando/plantilla/index.html')
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context(diccionario)
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)

def usando_loader(request):
    nombre = "Tadeo"
    apellido = "Junco"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)



def curso(request, nombre, numero):
    curso = curso(nombre=nombre, camada=int(numero))
    curso.save()
    documento = f"Curso: {curso.nombre}<br>Camada: {curso.camada}"
    return HttpResponse(documento)
