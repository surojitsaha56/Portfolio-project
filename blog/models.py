from django.db import models

# Create your models here.
#title
#date
#body
#image
#Add the blog app to the settings
#Create a migration
#Migrate
#Add to the admin

class Blog(models.Model):
    title= models.CharField(max_length=20)
    date= models.DateTimeField()
    body= models.TextField(max_length=200)
    image=models.ImageField(upload_to="images/")

