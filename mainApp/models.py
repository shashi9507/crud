from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=11)
    Designation = models.CharField(max_length=11)
    salery = models.IntegerField()
    city = models.CharField(max_length=50,null=True,blank=True,default="")
    state = models.CharField(max_length=20,null=True,blank=True,default="")
    def __str__(self):
        return str(self.id)+" / "+self.name+" / "+self.email