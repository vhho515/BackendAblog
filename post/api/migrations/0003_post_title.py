# Generated by Django 3.0.7 on 2021-12-09 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_post_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='DEFAULT VALUE', max_length=50),
        ),
    ]