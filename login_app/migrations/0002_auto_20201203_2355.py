# Generated by Django 2.2 on 2020-12-04 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='birthday',
            field=models.DateField(),
        ),
    ]
