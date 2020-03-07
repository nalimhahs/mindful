# Generated by Django 3.0.3 on 2020-03-07 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdata', '0006_auto_20200306_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='anxiety_quiz_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='current_medications',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='depression_quiz_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientdata',
            name='lifestyle_quiz_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
