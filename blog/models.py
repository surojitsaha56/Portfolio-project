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
    body= models.TextField(max_length=100)
    image=models.ImageField(upload_to="images/")

    def date2(self):
        return self.date.strftime('%b %e %Y')

    def __str__(self):
        return self.title


