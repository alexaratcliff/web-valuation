# Generated by Django 2.1.1 on 2019-02-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190225_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='created_by',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
    ]
