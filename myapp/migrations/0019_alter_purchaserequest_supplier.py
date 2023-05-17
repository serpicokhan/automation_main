# Generated by Django 3.2.6 on 2023-05-17 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_purchaserequest_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='myapp.business'),
        ),
    ]
