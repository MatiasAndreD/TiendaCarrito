# Generated by Django 3.0.9 on 2020-08-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=2000)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
