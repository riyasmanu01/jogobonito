# Generated by Django 3.1.7 on 2021-07-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_footballposistion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('tutorial', models.CharField(max_length=200)),
                ('video_name', models.CharField(max_length=200)),
                ('video_src', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='FootballPosistion',
        ),
        migrations.DeleteModel(
            name='Sports',
        ),
    ]
