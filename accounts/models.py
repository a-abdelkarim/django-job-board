from django.db import models
from django.contrib.auth.models import User

#import signals
from django.db.models.signals import post_save
from django.dispatch import receiver




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City' ,related_name='user_city' , on_delete=models.CASCADE, null=True, blank=True)
    phone =models.CharField(max_length=20)
    profile_pic = models.ImageField(default='no-image.png', upload_to = 'profile/')

    def __str__(self):
        return str(self.user) + "'s Profile"



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



class City(models.Model):
    name = models.CharField(max_length=15)
    
