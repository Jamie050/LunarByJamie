from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user   = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg',upload_to="profile_images",null=False,blank=False)
    bio = models.TextField(default="something interesting about me",blank=True,null=True)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200,blank=False,null=False)
    content = models.TextField(max_length=400,blank=False,null=False)
    thumbnail = models.ImageField(upload_to="post_images",null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
        
    def __str__(self):
        return self.subject



#create a profile when a new user is created
def create_user_profile(sender, instance, created, **kwargs):
       if created:
           UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
