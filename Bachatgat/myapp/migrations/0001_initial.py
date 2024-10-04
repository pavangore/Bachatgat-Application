# Generated by Django 5.1.1 on 2024-10-01 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BachatGatRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bachatgat_name', models.CharField(max_length=255)),
                ('start_month', models.CharField(max_length=50)),
                ('start_year', models.CharField(max_length=4)),
                ('chairperson_title', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.')], max_length=5)),
                ('chairperson_name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
