# Generated by Django 2.1.1 on 2018-09-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('celular', models.CharField(max_length=17)),
            ],
        ),
    ]
