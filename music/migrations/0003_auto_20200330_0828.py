# Generated by Django 2.2.4 on 2020-03-30 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_rating'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('song', 'user'), name='unique_rating'),
        ),
    ]