# Generated by Django 3.2.9 on 2022-03-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guild', '0002_alter_guildsetting_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='raidgroup',
            name='primary',
            field=models.BooleanField(default=False),
        ),
    ]
