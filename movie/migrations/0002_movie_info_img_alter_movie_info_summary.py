# Generated by Django 5.1.1 on 2024-10-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_info',
            name='img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='movie_info',
            name='Summary',
            field=models.TextField(null=True),
        ),
    ]
