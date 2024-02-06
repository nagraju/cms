# Generated by Django 5.0.1 on 2024-02-06 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbts', '0003_alter_students_fphno_alter_students_phno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='aadharno',
            field=models.CharField(default='111111111111', max_length=22),
        ),
        migrations.AlterField(
            model_name='students',
            name='dateofjoining',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='students',
            name='macno',
            field=models.CharField(default='1234', max_length=22),
        ),
        migrations.AlterField(
            model_name='students',
            name='odissueddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='polycetrank',
            field=models.IntegerField(default=1234),
        ),
        migrations.AlterField(
            model_name='students',
            name='sacno',
            field=models.CharField(default='1111', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='sbranch',
            field=models.CharField(default='CME', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='sschallticketno',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AlterField(
            model_name='students',
            name='sscrank',
            field=models.IntegerField(default=1234),
        ),
    ]
