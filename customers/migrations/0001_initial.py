# Generated by Django 2.0.7 on 2023-03-01 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('credit', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
