# Generated by Django 3.0.7 on 2020-06-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20200625_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='Cruz', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='year_level',
            field=models.CharField(default='Grade 1', max_length=100),
            preserve_default=False,
        ),
    ]
