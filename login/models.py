from django.db import models
# from django.utils import timezone

class Activity(models.Model):
    typ = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()


    # def __str__(self):
    #    return self.typ

