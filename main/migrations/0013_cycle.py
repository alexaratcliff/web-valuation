# Generated by Django 2.1.1 on 2019-03-13 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_outcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('semester', models.CharField(max_length=200)),
                ('outcomes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Outcome')),
                ('rubrics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Rubric')),
            ],
        ),
    ]
