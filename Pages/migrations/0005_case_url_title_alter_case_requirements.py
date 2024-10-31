# Generated by Django 5.1.1 on 2024-10-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0004_casecategory_client_alter_process_service_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='url_title',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='requirements',
            field=models.TextField(null=True),
        ),
    ]
