# Generated by Django 4.0.2 on 2022-02-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1500)),
                ('created', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
