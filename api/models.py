from django.db import models

# Create your models here.


#creating company table
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50,blank= False,unique=True)
    location = models.CharField(max_length=50)
    about = models.TextField(max_length=200)
    type = models.CharField(max_length=100,choices = (('IT','IT'),
    ('Finance','Finance'),
    ('AutoMobile','AutoMobile'),
    ('Steel','Steel')
    ))

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
         return f"{self.Name} : Id ---> {self.company_id}"

