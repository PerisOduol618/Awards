from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



class Profile(models.Model):
    profile_pic = models.ImageField( upload_to='profile/', blank ='true',default='default.png')
    bio = models.TextField()
    user =models.OneToOneField(User, on_delete = models.CASCADE)
    date_craeted= models.DateField(auto_now_add=True )

    def __str__(self):
        return f'{self.user.username} Profile'

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)

class Project(models.Model):
    title = models.TextField(max_length=30)
    image = models.ImageField(upload_to = 'home/')
    link= models.URLField(max_length=200)
    description = models.TextField(max_length=300)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE)
    date_craeted= models.DateField(auto_now_add=True )
    

    def __str__(self):
        return self.title



   
    


