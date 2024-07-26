from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
	return HttpResponse("Hola arrancando con el proyecto!")
def dia_de_hoy (request):
	dia = datetime.now()
	return HttpResponse(f"Hoy es día:<br>{dia}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a el proyecto de Tade")


def probando_template(request): 
	mi_html = open('./Practicando/plantilla/index.html')
	plantilla = Template(mi_html.read())
	mi_html.close()
	mi_contexto = Context()
	documento = plantilla.render(mi_contexto)
	return HttpResponse(documento)

	
	
		
	