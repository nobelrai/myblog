# Generated by Django 4.2.7 on 2024-06-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_education_end_date_alter_experience_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
