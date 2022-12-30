# Generated by Django 3.2.6 on 2022-12-26 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_requestfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestVoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msgFile', models.FileField(max_length=200, upload_to='documents/%Y/%m/%d')),
                ('msgFiledateAdded', models.DateTimeField(auto_now_add=True)),
                ('msgFileworkorder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.purchase')),
            ],
            options={
                'db_table': 'requestvoice',
            },
        ),
    ]