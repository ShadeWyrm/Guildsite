# Generated by Django 3.2.9 on 2022-03-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0007_raidgroup_raid_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='public_note',
            field=models.TextField(default=''),
        ),
    ]