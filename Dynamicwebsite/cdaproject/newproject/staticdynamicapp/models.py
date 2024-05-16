from django.db import models

# Create your models here.


# Create your models here.
class Bigd(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='picsa')
    des=models.TextField()
    def __str__(self):
        return self.name
class Great(models.Model):    
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='picsart')
    des1=models.TextField()    
    def __str__(self):
        return self.name1
class Goose(models.Model):    
    name2=models.CharField(max_length=250)
    img2=models.ImageField(upload_to='picsarss')
    des2=models.TextField()    
    def __str__(self):
        return self.name2
class Goofy(models.Model):    
    name3=models.CharField(max_length=250)
    img3=models.ImageField(upload_to='picsard')
    des3=models.TextField()    
    def __str__(self):
        return self.name3    
class Gog(models.Model):    
    name4=models.CharField(max_length=250)
    img4=models.ImageField(upload_to='picsardds')
    des4=models.TextField()    
    def __str__(self):
        return self.name4    
  
