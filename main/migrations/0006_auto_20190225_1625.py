# Generated by Django 2.1.1 on 2019-02-25 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190225_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryTitle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measureTitle', models.CharField(max_length=200)),
                ('measureText', models.CharField(max_length=200)),
                ('weight', models.PositiveIntegerField(default=1, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='rubric',
            name='measureText',
        ),
        migrations.RemoveField(
            model_name='rubric',
            name='weight',
        ),
        migrations.AddField(
            model_name='rubric',
            name='assigned_to',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='main.Evaluator'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rubric',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Administrator'),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Measure'),
        ),
    ]