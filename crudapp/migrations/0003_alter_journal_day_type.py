# Generated by Django 5.1.3 on 2024-11-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_alter_journal_day_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='day_type',
            field=models.CharField(max_length=10),
        ),
    ]
