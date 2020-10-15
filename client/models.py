from django.db import models
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254,unique=True)
    active = models.BooleanField(default=True)
    location = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    def __str__(self) :
        return f"{self.first_name} {self.last_name}"

class ClientDetail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,related_name="client")
    deadline = models.DateField(blank=True,null=True)
    project_title = models.CharField(max_length=50)
    project_description = models.TextField(blank=True)
    total_expense  = MoneyField(max_digits=14, decimal_places=2, default_currency='INR')
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self) :
        return f"{self.project_title}"

    


