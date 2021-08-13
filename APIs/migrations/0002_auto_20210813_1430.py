# Generated by Django 3.2 on 2021-08-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='satisfaction',
            field=models.CharField(choices=[('1', '1'), ('4', '4'), ('5', '5'), ('3', '3'), ('2', '2')], max_length=10, verbose_name='만족도'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
    ]
