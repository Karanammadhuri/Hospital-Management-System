from django.db import models
from django.utils import timezone

# Create your models here.
class Patient(models.Model):
    pid = models.CharField(max_length=20)
    pname = models.CharField(max_length=100)
    pdisease = models.CharField(max_length=500)
    pspecalist = models.CharField(max_length=100)
    pcontact = models.CharField(max_length=10)
    ptimings = models.TimeField(default=timezone.now())
    pbook_date = models.DateField(default=timezone.now())


    class Meta:
        db_table = "patient"
