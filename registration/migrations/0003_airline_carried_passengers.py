# Generated by Django 4.2 on 2023-04-10 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_airline_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='carried_passengers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
