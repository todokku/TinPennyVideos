# Generated by Django 2.2.4 on 2019-09-20 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20190919_0338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='user',
            new_name='publisher',
        ),
        migrations.AddField(
            model_name='video',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='is private?'),
        ),
    ]