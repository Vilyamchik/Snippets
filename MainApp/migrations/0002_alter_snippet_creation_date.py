# Generated by Django 4.2 on 2024-01-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
