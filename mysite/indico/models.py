from django.db import models
# from django.utils.text import slugify
from solo.models import SingletonModel
# Create your models here.

class SliderItem(models.Model):
    greating_text= models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=50)
    image=models.ImageField(upload_to="slider/")
    button_one = models.URLField()
    
    def __str__(self):
        return self.title
    
class Slider(SingletonModel):
    name = models.CharField(max_length=20)
    slider_item = models.ManyToManyField(SliderItem)

class AboutItem(models.Model):
    image=models.ImageField(upload_to="aboutitem/")
    title=models.CharField(max_length=50)
    desc=models.TextField()
    def __str__(self) :
        return f"{self.title}"
    
class About(SingletonModel):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    aboutItem=models.ManyToManyField(AboutItem)

