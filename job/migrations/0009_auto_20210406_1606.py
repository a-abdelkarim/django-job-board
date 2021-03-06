# Generated by Django 3.1.7 on 2021-04-06 14:06

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='img',
            field=models.ImageField(default='no-image.png', upload_to=job.models.image_upload),
        ),
    ]
