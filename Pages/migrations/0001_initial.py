# Generated by Django 5.1.1 on 2024-10-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url_title', models.SlugField()),
                ('big_image', models.ImageField(upload_to='images/')),
                ('small_image', models.ImageField(upload_to='images/')),
                ('approach', models.TextField()),
                ('what_we_offer', models.TextField()),
                ('tags', models.CharField(max_length=255)),
                ('mini_image_text', models.TextField()),
                ('process_text', models.TextField()),
            ],
        ),
    ]
