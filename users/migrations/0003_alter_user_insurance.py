# Generated by Django 4.1.1 on 2024-06-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='insurance',
            field=models.IntegerField(),
        ),
    ]
