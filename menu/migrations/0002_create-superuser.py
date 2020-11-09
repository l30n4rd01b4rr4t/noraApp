# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.auth.models import User


def create_superuser(apps, schema_editor):
       User.objects.create_superuser(username='admin', password='n0r44dm1n', email='nora@menuapp.com')


class Migration(migrations.Migration):

       dependencies = [('menu', '0001_initial'),]

       operations = [migrations.RunPython(create_superuser)]