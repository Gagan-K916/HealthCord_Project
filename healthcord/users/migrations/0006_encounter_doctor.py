# Generated by Django 5.0 on 2023-12-22 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_encounter'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='doctor',
            field=models.EmailField(default='doctor.unknown@example.com', max_length=254),
            preserve_default=False,
        ),
    ]
