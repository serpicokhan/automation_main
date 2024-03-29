# Generated by Django 3.2.6 on 2023-01-10 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_sysuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCsvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgFile', models.FileField(max_length=200, upload_to='documents/%Y/%m/%d')),
                ('msgFiledateAdded', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'businesscsvfile',
            },
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='PurchaseRequestRequestedUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PurchaseRequestdUser2', to='myapp.sysuser', verbose_name='کاربر درخواست کننده'),
        ),
    ]
