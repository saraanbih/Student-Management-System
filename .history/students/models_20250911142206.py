from django.db import models

# Create your models here.

class Studnet(models.Model):
  student_number = models.PositiveBigIntegerField
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()

  


    