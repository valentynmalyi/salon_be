# Generated by Django 3.2.18 on 2023-03-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='asd',
            field=models.BooleanField(default=False),
        ),
    ]
