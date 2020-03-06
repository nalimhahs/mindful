# Generated by Django 3.0.3 on 2020-03-06 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anxiety_quiz_score', models.IntegerField()),
                ('depression_quiz_score', models.IntegerField()),
                ('current_medications', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SleepData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light', models.IntegerField()),
                ('deep', models.IntegerField()),
                ('rem', models.IntegerField()),
                ('awake', models.IntegerField()),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdata.PatientData')),
            ],
        ),
        migrations.CreateModel(
            name='PressureData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.IntegerField()),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdata.PatientData')),
            ],
        ),
        migrations.CreateModel(
            name='FoodData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apettite', models.IntegerField(choices=[('0', 'Very poor'), ('0', 'poor'), ('0', 'fair'), ('0', 'good'), ('0', 'very good')])),
                ('date', models.DateField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientdata.PatientData')),
            ],
        ),
    ]
