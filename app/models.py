from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    mobile_no=models.BigIntegerField()
    address=models.CharField(max_length=20)
    courses=models.CharField(max_length=20)

    def __str__(self):
        return self.name
