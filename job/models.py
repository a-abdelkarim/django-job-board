from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import random

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

def image_upload(instance, filename):
    imagname, extention = filename.split('.')
    return "jobs/%s_%s_%s.%s"%(instance.id, instance.title, instance.published_at, extention)

class Job(models.Model):
    user = models.ForeignKey(User, related_name='job_publisher', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    img = models.ImageField(upload_to=image_upload, default='no-image.png')
    descrption = models.TextField(max_length=1000, null=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)

    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        title = slugify(self.title)
        r1 = random.random()
        r2 = random.random()
        r3 = random.random()
        r4 = random.random()
        sum_r = (r1+r2)*(r3)*(r4)
        
        self.slug = '%s-%s'%(title, sum_r)

        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Candidate(models.Model):
    job = models.ForeignKey(Job, related_name='cnadidate', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField()
    resume = models.FileField(upload_to='cnadidates')
    cover_letter = models.TextField(max_length=500)
    applied_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + self.email