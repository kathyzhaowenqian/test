from django.db import models

# Create your models here.
#models.py中
class ADAIADAI(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class Meta:
        db_table = 'ADAIADAIdocker3'