# Generated by Django 3.0.6 on 2020-05-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
