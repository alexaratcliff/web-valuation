# Generated by Django 2.1.1 on 2019-02-26 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190225_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluate_rubric',
            name='evaluator',
        ),
        migrations.AlterField(
            model_name='evaluate_rubric',
            name='rubric',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='evaluate_rubric',
            name='student',
            field=models.CharField(max_length=200),
        ),
    ]
