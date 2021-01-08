from django.db import models

# Create your models here.
class date_time(models.Model):
    dat = models.CharField(max_length = 10, blank = False)
    tim = models.CharField(max_length = 10, blank = False)
    status = models.CharField(max_length = 3)
