# Generated by Django 3.2.9 on 2022-03-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0011_auto_20220328_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='public_note',
        ),
        migrations.AddField(
            model_name='member',
            name='public_note',
            field=models.TextField(blank=True, default=''),
        ),
    ]