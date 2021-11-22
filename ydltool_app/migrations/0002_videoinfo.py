# Generated by Django 3.2.9 on 2021-11-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ydltool_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='videoInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('video_id', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('json_data', models.JSONField(blank=True, default=dict, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
