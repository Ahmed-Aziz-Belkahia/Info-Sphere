# Generated by Django 5.1.1 on 2024-10-29 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_service_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Pages.service'),
        ),
    ]
