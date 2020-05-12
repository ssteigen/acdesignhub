# Generated by Django 3.0.6 on 2020-05-12 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0008_increase_max_length_design_and_creator_codes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='design',
            old_name='creator',
            new_name='creator_name',
        ),
        migrations.AddField(
            model_name='design',
            name='creator_island',
            field=models.CharField(default='default', max_length=10),
            preserve_default=False,
        ),
    ]