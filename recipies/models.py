from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.



class Category(models.Model):
    name = CharField(max_length=64, unique=True)


    def __str__(self):
        return self.name

class Recipie(models.Model):
    title = CharField(max_length=64, unique=True)
    body = TextField()
    category = models.ManyToManyField(Category, blank=True) 

    def __str__(self):
        return self.title


