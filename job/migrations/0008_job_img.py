# Generated by Django 3.1.7 on 2021-04-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='img',
            field=models.ImageField(default='empty.png', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]