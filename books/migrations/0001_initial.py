# Generated by Django 2.2.6 on 2022-04-20 20:55

import books.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=2000.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IssuedBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField(auto_now=True)),
                ('due_date', models.DateField(default=books.models.expiry)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('is_lost', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
    ]
