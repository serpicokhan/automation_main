# Generated by Django 3.2.6 on 2023-01-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20230103_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysuser',
            name='phone',
            field=models.CharField(blank=True, max_length=70, null=True, unique=True, verbose_name='موبایل'),
        ),
    ]
