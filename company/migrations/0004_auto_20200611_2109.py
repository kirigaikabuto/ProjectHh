# Generated by Django 3.0.7 on 2020-06-11 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_vacancy_elective'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='company.Company'),
        ),
    ]
