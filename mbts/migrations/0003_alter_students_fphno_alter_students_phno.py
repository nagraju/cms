# Generated by Django 5.0.1 on 2024-02-06 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbts', '0002_remove_students_studycertificateissudedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='fphno',
            field=models.CharField(default='123445654', max_length=12),
        ),
        migrations.AlterField(
            model_name='students',
            name='phno',
            field=models.CharField(default='123456', max_length=12),
        ),
    ]
