from django.db import models

# Create your models here.

class Football(models.Model):
    position = models.CharField(max_length=200)
    tutorial = models.CharField(max_length=200)
    video_name = models.CharField(max_length=200)
    video_src = models.CharField(max_length=200)

class register(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class websitename(models.Model):
    name = models.CharField(max_length=200)
    logo = models.FileField(upload_to='images/', null=True, blank=True)

class features(models.Model):
    featurename = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')
    description = models.CharField(max_length=200)

class socialmedia(models.Model):
    name = models.CharField(max_length=200)
    icon = models.FileField(upload_to='images/')
    link = models.CharField(max_length=200)


class tutorialssports(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')
    icon = models.FileField(upload_to='images/')

class sportsposition(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')

class tutorialvideos(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    tutorial = models.CharField(max_length=200)
    video_name = models.CharField(max_length=200)
    video_src = models.CharField(max_length=200)

class admindata(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)