# Generated by Django 2.0.4 on 2018-04-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saferdb', '0007_auto_20180422_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='cardUrl',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
