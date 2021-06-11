# Generated by Django 3.1.2 on 2020-10-15 10:15

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Causes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique_for_date='publish')),
                ('cause_image', models.ImageField(upload_to='CauseImage/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]