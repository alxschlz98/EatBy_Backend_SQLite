# Generated by Django 3.0.5 on 2020-05-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_remove_pantry_idno'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantry',
            name='idNo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='idNo',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
