from django.db import models

# Create your models here.

class Number(models.Model):
    no = models.IntegerField()

    def __str__(self):
        return str(self.no)

class Word(models.Model):
    name = models.CharField(max_length=50)
    number = models.OneToOneField(Number, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
