from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_Pics',blank=True,null=True)
    about = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.user.username

class addcategory(models.Model):
    class Meta:
        verbose_name = 'addcategory'
        verbose_name_plural = 'addcategories'
    category = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.category
    
class photo(models.Model):
    user = models.ForeignKey(User,null = True,blank=True,on_delete=models.CASCADE)
    categories = models.ForeignKey(addcategory,null=True,blank=True,on_delete=models.SET_NULL)

    title = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.title