# Generated by Django 3.2.7 on 2021-11-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20211125_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='was_absent',
            field=models.BooleanField(default=False, verbose_name='Was absent'),
        ),
    ]
