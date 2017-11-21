# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# from django.db import models
from django.contrib.gis.db import models


# This model has been generated automatically through inspectdb
class Gewaspercelen2016(models.Model):
    objectid = models.DecimalField(unique=True, max_digits=65535, decimal_places=65535)
    geom = models.MultiPolygonField(srid=28992)  # This field type is a guess.
    cat_gewasc = models.CharField(max_length=60, blank=True, null=True)
    gws_gewasc = models.CharField(max_length=10, blank=True, null=True)
    geometrie_field = models.DecimalField(db_column='geometrie_', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field renamed because it ended with '_'.
    geometri_1 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    gws_gewas = models.CharField(max_length=254, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gewaspercelen2016'
