# Generated by Django 2.1 on 2018-08-30 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperatures', '0003_school_schoolname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempreading',
            name='date',
            field=models.DateTimeField(verbose_name='Date Recorded'),
        ),
    ]
