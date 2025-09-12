from django.db import models

# Create your models here.

class Studnet(models.Model):
  student_number = models.PositiveBigIntegerField
  first_name = models.CharField(max_length=50)
    