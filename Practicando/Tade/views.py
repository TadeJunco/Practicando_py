from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def inicio(request):
    return HttpResponse("Vista inicio")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")


	

