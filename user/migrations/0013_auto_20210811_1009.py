# Generated by Django 3.1.7 on 2021-08-11 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='websitename',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]