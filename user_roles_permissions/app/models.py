from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Permission(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.id


class Role(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    permissions = models.ManyToManyField(Permission, null=True, blank=True)

    def __unicode__(self):
        return self.id

class User(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    roles = models.ManyToManyField(Role, null=True, blank=True)

    def __unicode__(self):
        return self.id

