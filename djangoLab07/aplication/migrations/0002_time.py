# Generated by Django 4.2.3 on 2023-07-25 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=20)),
                ('temperature', models.CharField(max_length=5)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]