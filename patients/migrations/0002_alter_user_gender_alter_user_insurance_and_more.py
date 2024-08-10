# Generated by Django 4.1.1 on 2024-08-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('man', 'muž'), ('woman', 'žena'), ('non-binary', 'nebinární')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='insurance',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='role_patient',
            field=models.TextField(choices=[('Doctor', 'doktor'), ('Nurse', 'zdravotní sestra'), ('Patient', 'pacient')]),
        ),
    ]
