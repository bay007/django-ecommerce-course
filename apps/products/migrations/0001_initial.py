# Generated by Django 2.2.5 on 2019-09-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Nombre producto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('description', models.TextField(max_length=255, verbose_name='Descripción')),
            ],
        ),
    ]
