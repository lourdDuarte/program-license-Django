# Generated by Django 4.1 on 2022-09-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RequestsLicense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestslicense',
            name='date_form',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='requestslicense',
            name='date_to',
            field=models.CharField(max_length=25),
        ),
    ]