# Generated by Django 3.2.6 on 2023-01-03 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_partcsvfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaserequest',
            name='PurchaseRequestCompletionDate',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ تکمیل'),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='PurchaseRequestRequestedUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PurchaseRequestdUser2', to='myapp.sysuser', verbose_name='کاربر درخواست کننده'),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='PurchaseRequestStatus',
            field=models.IntegerField(blank=True, choices=[(1, 'درخواست شده'), (2, 'متوقف'), (4, 'تخصیص داده شده'), (5, 'باز'), (6, 'در حال پیشرفت'), (7, 'بسته شده کامل'), (8, 'بسته شده، ناقص'), (9, 'در انتظار قطعه')], null=True, verbose_name='وضعیت درخواست'),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='PurchaseRequestTayeedUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PurchaseAdmitter2', to='myapp.sysuser', verbose_name='کاربر تایید کننده'),
        ),
    ]
