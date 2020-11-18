from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    image=models.ImageField(upload_to='cover_pics',default='default.png')
    email=models.EmailField(max_length=254)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date']
        
        
        
