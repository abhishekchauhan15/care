# Generated by Django 2.2.11 on 2023-04-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0350_auto_20230422_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpatientregistration',
            name='action',
            field=models.IntegerField(blank=True, choices=[(10, 'NO_ACTION'), (20, 'PENDING'), (30, 'SPECIALIST_REQUIRED'), (40, 'PLAN_FOR_HOME_CARE'), (50, 'FOLLOW_UP_NOT_REQUIRED'), (60, 'COMPLETE'), (70, 'REVIEW'), (80, 'NOT_REACHABLE')], default=10, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='action',
            field=models.IntegerField(blank=True, choices=[(10, 'NO_ACTION'), (20, 'PENDING'), (30, 'SPECIALIST_REQUIRED'), (40, 'PLAN_FOR_HOME_CARE'), (50, 'FOLLOW_UP_NOT_REQUIRED'), (60, 'COMPLETE'), (70, 'REVIEW'), (80, 'NOT_REACHABLE')], default=10, null=True),
        ),
    ]
