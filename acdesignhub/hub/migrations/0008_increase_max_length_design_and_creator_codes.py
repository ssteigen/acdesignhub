# Generated by Django 3.0.6 on 2020-05-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0007_rename_designer_to_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='creator_code',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='design',
            name='design_code',
            field=models.CharField(max_length=17),
        ),
    ]
