# Generated by Django 4.2.4 on 2024-03-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nouapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
