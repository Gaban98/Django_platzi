from django.shortcuts import render
from django.http import HttpResponse



def index (request):
    return HttpResponse("Pagina principal de la app de premios")


def detail(request, question_id):
    #aca recibe de parametro el id de la pregunta
    return HttpResponse(f"Estas viendo la pregunta numero {question_id}")

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta {question_id}")