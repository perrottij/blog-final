# Generated by Django 2.2 on 2019-06-04 13:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
            ],
        ),
    ]
