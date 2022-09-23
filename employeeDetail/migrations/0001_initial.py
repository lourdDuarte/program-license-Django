# Generated by Django 4.1 on 2022-09-23 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antiquity', models.CharField(max_length=15)),
                ('leave_days', models.CharField(max_length=25)),
                ('remainder', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=25)),
                ('created', models.DateField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
