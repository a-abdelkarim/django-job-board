# Generated by Django 3.1.7 on 2021-04-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='descrption',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
