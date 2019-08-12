# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Recipe(models.Model):
  id = models.IntegerField(db_column='ID', primary_key=True)
  name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)
  ingredients = models.CharField(db_column='Ingredients', max_length=1000, blank=True, null=True)
  instructions = models.TextField(db_column='Instructions', blank=True, null=True)
  total_time = models.CharField(db_column='Total_Time', max_length=20, blank=True, null=True)
  servings = models.TextField(db_column='Servings', blank=True, null=True)
  img_name = models.CharField(db_column='Img_Name', max_length=20, blank=True, null=True)
  rating = models.TextField(db_column='Rating', blank=True, null=True)

  class Meta:
      managed = False
      db_table = 'recipes'
