# Generated by Django 3.1.7 on 2021-03-30 15:59

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_auto_20210329_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Near',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.plugin',),
        ),
    ]
