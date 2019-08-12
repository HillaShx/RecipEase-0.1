# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Recipes(models.Model):
    id = models.IntegerField(db_column='ID')
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)
    ingredients = models.CharField(db_column='Ingredients', max_length=1000, blank=True, null=True)
    instructions = models.TextField(db_column='Instructions', blank=True, null=True)
    total_time = models.CharField(db_column='Total_Time', max_length=20, blank=True, null=True)
    servings = models.TextField(db_column='Servings', blank=True, null=True) This field type is a guess.
    img_name = models.CharField(db_column='Img_Name', max_length=20, blank=True, null=True)
    rating = models.TextField(db_column='Rating', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipes'
