from django.shortcuts import render
from django.http import HttpResponse
from .models import Question



def index (request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    #esto guarda en una variable la lista de preguntas
    return render(request, "polls/index.html", context)
# el primer parametro es el request, el segundo es el template que se va a renderizar
#el tercer parametro es un diccionario que se le pasa al template
#el diccionario es el contexto, es decir, las variables que se van a usar en el template


def detail(request, question_id):
    #aca recibe de parametro el id de la pregunta
    return HttpResponse(f"Estas viendo el detalle pregunta numero {question_id}")

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados numero {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta {question_id}")