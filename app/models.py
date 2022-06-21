from pydoc import describe
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.

class Neighbourhood(models.Model):
    image=CloudinaryField('image', null=True)
    describe = models.TextField(null=True)
    name =models.CharField(max_length=50 , null=True)
    neighbourhood_location = models.CharField(max_length=100, null=True)
    occupants_count= models.IntegerField(default=0)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    health_contacts = models.CharField(max_length=20, null=True, blank=True)
    police_contacts = models.CharField(max_length=20, null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    
    def save_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()
        
    def update_neighbourhood(self):
        self.update()
        