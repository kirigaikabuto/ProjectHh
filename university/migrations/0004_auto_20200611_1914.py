# Generated by Django 3.0.7 on 2020-06-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0003_auto_20200611_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='datebirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]