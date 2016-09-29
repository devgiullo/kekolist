from django.db import models

# Create your models here.


class List(models.Model):
    name_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    exp_date = models.DateTimeField('expiration date')
    completed_bool = models.BooleanField(default=False)
    #list_id = models.IntegerField(default=0)
    list_id = models.ForeignKey(List, default=None)


class Collaborator(models.Model):
    task_id = models.IntegerField()
    user_id = models.IntegerField()
