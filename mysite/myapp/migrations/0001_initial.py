# Generated by Django 5.0.1 on 2024-01-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, max_length=1000, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
