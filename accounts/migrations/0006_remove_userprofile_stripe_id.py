# Generated by Django 2.0 on 2018-04-22 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userprofile_stripe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='stripe_id',
        ),
    ]