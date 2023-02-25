from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    #< .... > esa expresión es la forma en que django nos da de poder pasar variables o datos
    #si yo entro a /polls/5/ me va a mostrar la pregunta 5
    path('<int:question_id>/results/', views.result, name='result'),
    #ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #ex: /polls/5/vote/
    #se enlaza con el views a las vistas creadas 
]

