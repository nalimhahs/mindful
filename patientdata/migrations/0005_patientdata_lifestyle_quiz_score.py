# Generated by Django 3.0.3 on 2020-03-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patientdata', '0004_auto_20200306_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdata',
            name='lifestyle_quiz_score',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
