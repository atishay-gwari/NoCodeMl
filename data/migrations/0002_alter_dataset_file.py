# Generated by Django 4.0.6 on 2023-10-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='file',
            field=models.FileField(upload_to='dataset/'),
        ),
    ]
