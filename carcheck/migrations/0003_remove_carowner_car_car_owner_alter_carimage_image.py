# Generated by Django 4.1 on 2023-04-26 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carcheck', '0002_carowner_carimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carowner',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carcheck.carowner'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.ImageField(upload_to='cars'),
        ),
    ]
