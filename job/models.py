from django.db import models
from django.utils.text import slugify

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

def image_upload(instance, filename):
    imagname, extention = filename.split('.')
    return "jobs/%s_%s_%s.%s"%(instance.id, instance.title, instance.published_at, extention)

class Job(models.Model):
    
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
        self.slug = 'AsVbQr3RfVZcGJhjT%sErBfXs%s'%(slugify(self.title), self.id)

        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name