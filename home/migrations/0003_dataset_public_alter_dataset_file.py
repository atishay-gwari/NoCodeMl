# Generated by Django 4.0.6 on 2023-10-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_datasets_dataset'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
