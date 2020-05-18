# Generated by Django 3.0.6 on 2020-05-17 16:57

import acdesignhub.hub.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0011_auto_20200515_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='design',
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=acdesignhub.hub.models._upload_path)),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.Design')),
            ],
        ),
    ]