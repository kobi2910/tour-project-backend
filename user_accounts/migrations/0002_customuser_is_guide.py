# Generated by Django 4.0.10 on 2024-01-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_guide',
            field=models.BooleanField(default=False),
        ),
    ]