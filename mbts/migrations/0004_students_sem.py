# Generated by Django 5.0.1 on 2024-02-14 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbts', '0003_alter_students_aadharno_alter_students_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='sem',
            field=models.CharField(max_length=20, null=True),
        ),
    ]