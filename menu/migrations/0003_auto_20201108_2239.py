# Generated by Django 3.1.3 on 2020-11-09 01:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_create-superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='ID único para este plato', primary_key=True, serialize=False),
        ),
    ]