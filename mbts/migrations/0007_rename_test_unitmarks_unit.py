# Generated by Django 5.0 on 2024-03-20 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mbts', '0006_alter_unit1marks_s1_alter_unit1marks_s10_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unitmarks',
            old_name='test',
            new_name='unit',
        ),
    ]
