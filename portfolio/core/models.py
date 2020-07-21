# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"  

# Service model
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill name")
    description = models.TextField(verbose_name="About skill")

    def __str__(self):
        return self.name

# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

#Client Model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name

                


