# Generated by Django 4.0.10 on 2024-02-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_trip_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='area',
            field=models.CharField(blank=True, choices=[('GO', 'Golan'), ('GA', 'Galil'), ('NEG', 'Negev'), ('JRU', 'Jerusalem'), ('TA', 'Tel Aviv')], max_length=10, null=True),
        ),
    ]
