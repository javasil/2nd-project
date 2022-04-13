from django.db import models
from versatileimagefield.fields import VersatileImageField


class Blog(models.Model):
     CATEGORY_CHOICES =(('agency','Agency'),('digital','Digital'),('branding','Branding'),)

     title = models.CharField(max_length=128)
     slug = models.SlugField(unique=True,blank=True, null=True)
     category = models.CharField(max_length=120,choices = CATEGORY_CHOICES,default="creative")
     content = models.TextField()
     author_name = models.CharField(max_length=120)
     featured_image = models.ImageField()
     description = models.TextField()
     image = models.ImageField()
     author = models.ForeignKey("Author",on_delete=models.CASCADE)

     def __str__(self):
        return str(self.title)


class Author(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    photo = models.ImageField()
    about = models.TextField()

    def __str__(self):
        return str(self.name)

     
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    place = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)
        
        
class Project(models.Model):
    CATEGORY_CHOICES =(('advertising','Advertising'),('branding','Branding'),)
        
    title = models.CharField(max_length=120)
    image = models.ImageField()
    category = models.CharField(max_length=120,choices = CATEGORY_CHOICES,default="branding")
    designation = models.CharField(max_length=120)
        
    def __str__(self):
        return str(self.title)
            
            
class Testimonial(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField
    name = models.CharField(max_length=120)

    def __str__(self):
        return str(self.title)  
        
      
class Slider(models.Model): 
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=120)
    link = models.URLField(max_length=190,blank=True)

    def __str__(self):
        return str(self.title)  
        
        
class Service(models.Model): 
    title = models.CharField(max_length=120)
    icon = models.FileField()
    description = models.TextField()
    
    def __str__(self):
        return str(self.title) 
        
            
            
            
        
        
        
        
        
        
