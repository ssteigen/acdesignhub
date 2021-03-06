# Generated by Django 3.0.6 on 2020-05-07 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0005_rename_submission_to_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='design_type',
            field=models.CharField(choices=[('BALLOON_HEM_DRESS', 'Balloon-hem dress'), ('BRIMMED_CAP', 'Brimmed cap'), ('BRIMMED_HAT', 'Brimmed hat'), ('COAT', 'Coat'), ('CUSTOM_DESIGN', 'Custom design'), ('HOODIE', 'Hoodie'), ('KNIT_CAP', 'Knit cap'), ('LONG_SLEEVE_DRESS', 'Long-sleeve dress'), ('LONG_SLEEVE_DRESS_SHIRT', 'Long-sleeve dress shirt'), ('ROBE', 'Robe'), ('ROUND_DRESS', 'Round dress'), ('SHORT_SLEEVE_DRESS', 'Short-sleeve dress'), ('SHORT_SLEEVE_TEE', 'Short-sleeve tee'), ('SLEEVELESS_DRESS', 'Sleeveless dress'), ('SWEATER', 'Sweater'), ('TANK_TOP', 'Tank top')], max_length=128),
        ),
    ]
