# Generated by Django 4.2.3 on 2023-07-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_orders_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='User name')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
            ],
        ),
    ]