# Generated by Django 3.1.7 on 2021-04-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_candidate_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='applied_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
