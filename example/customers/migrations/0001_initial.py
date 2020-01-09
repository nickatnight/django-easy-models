# Generated by Django 2.0 on 2020-01-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(blank=True, max_length=1)),
                ('age', models.IntegerField(blank=True)),
            ],
        ),
    ]
