# Generated by Django 3.2.23 on 2023-11-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20231111_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voetbalspelers',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='voetbalspelers',
            name='club',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
