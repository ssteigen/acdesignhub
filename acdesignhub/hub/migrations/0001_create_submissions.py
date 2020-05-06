# Generated by Django 3.0.6 on 2020-05-05 23:57

import acdesignhub.hub.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.FileField(max_length=1024, upload_to=acdesignhub.hub.models._upload_path)),
                ('name', models.CharField(max_length=255)),
                ('design_code', models.CharField(max_length=14)),
                ('description', models.TextField(blank=True, null=True)),
                ('username', models.CharField(max_length=10)),
                ('friend_code', models.CharField(max_length=14)),
            ],
        ),
    ]
