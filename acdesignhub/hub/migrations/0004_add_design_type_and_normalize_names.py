# Generated by Django 3.0.6 on 2020-05-06 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0003_rename_designer_metadata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='name',
            new_name='design_name',
        ),
        migrations.AddField(
            model_name='submission',
            name='design_type',
            field=models.CharField(choices=[('BALLOON_HEM_DRESS', 'Baloon-hem Dress'), ('BRIMMED_CAP', 'Brimmed cap'), ('BRIMMED_HAT', 'Brimmed hat'), ('COAT', 'Coat'), ('CUSTOM_DESIGN', 'Custom design'), ('HOODIE', 'Hoodie'), ('KNIT_CAP', 'Knit cap'), ('LONG_SLEEVE_DRESS', 'Long-sleeve dress'), ('LONG_SLEEVE_DRESS_SHIRT', 'Long-sleeve dress shirt'), ('ROBE', 'Robe'), ('ROUND_DRESS', 'Round dress'), ('SHORT_SLEEVE_DRESS', 'Short-sleeve dress'), ('SHORT_SLEEVE_TEE', 'Short-sleeve tee'), ('SLEEVELESS_DRESS', 'Sleeveless dress'), ('SWEATER', 'Sweater'), ('TANK_TOP', 'Tank top')], default='CUSTOM_DESIGN', max_length=128),
            preserve_default=False,
        ),
    ]
