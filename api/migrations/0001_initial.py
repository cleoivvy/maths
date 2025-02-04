# Generated by Django 5.1.5 on 2025-02-04 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumberProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('is_prime', models.BooleanField()),
                ('is_perfect', models.BooleanField()),
                ('properties', models.CharField(max_length=255)),
                ('digit_sum', models.IntegerField()),
                ('fun_fact', models.TextField()),
            ],
        ),
    ]
