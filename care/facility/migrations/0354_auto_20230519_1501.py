# Generated by Django 2.2.11 on 2023-05-19 09:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0353_auto_20230429_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file_type',
            field=models.IntegerField(choices=[(1, 'PATIENT'), (2, 'CONSULTATION'), (3, 'SAMPLE_MANAGEMENT'), (4, 'CLAIM'), (5, 'DISCHARGE_SUMMARY')], default=1),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dosage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='prescribed_by',
            field=models.ForeignKey(null=True, on_delete=models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='medicine',
            field=models.CharField(max_length=1023),
        ),
    ]
