# Generated by Django 3.2.6 on 2022-07-12 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220712_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaserequest',
            name='PurchaseRequestPurchase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='myapp.purchase'),
        ),
    ]
