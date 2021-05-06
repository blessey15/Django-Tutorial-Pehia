from django.db import models


# Create your models here.
class SampleTable(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return "sample"
