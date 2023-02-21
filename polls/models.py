from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    #el id genera la cable primaria de manera inmediata
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Fecha de publicación')
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    #restamos al tiempo actual 1 dia para que nos de el tiempo actual menos 1 dia
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #el de arriba es para unir la PK de la tabla question con la FK de la tabla choice
    #ademas los parametros on_delete=models.CASCADE es para que si se elimina una pregunta se eliminen sus respuestas
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #esto es como un contador de votos
    def __str__(self):
        return self.choice_text