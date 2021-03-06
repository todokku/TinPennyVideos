# Generated by Django 2.2.4 on 2019-10-03 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import media.models
import media.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of category')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('origin', models.FileField(upload_to=media.utils.path_and_rename)),
                ('origin_size_in_kb', models.IntegerField(blank=True, null=True, verbose_name='video size in kilobytes')),
                ('poster_thumbnail', media.models.S3PathField(blank=True, verbose_name='Path to poster frame for video')),
                ('duration_in_ms', models.IntegerField(blank=True, null=True, verbose_name='duration in milli seconds')),
                ('is_public', models.BooleanField(default=True, verbose_name='Is public?')),
                ('mc_status', models.CharField(choices=[('not_started', 'Not started'), ('started', 'Started'), ('succeeded', 'Succeeded'), ('failed', 'Failed')], default='not_started', help_text='Updated by celery jobs. Do not update manually', max_length=50, verbose_name='Media convert status')),
                ('failure_reason', models.TextField(blank=True, verbose_name='Failure reason of media convert')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='videos', to='media.Category')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('modified',),
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', media.models.S3PathField(verbose_name='Full S3 Path to converted video stream')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streams', to='media.Video')),
            ],
        ),
    ]
