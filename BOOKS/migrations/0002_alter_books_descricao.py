# Generated by Django 5.0.3 on 2024-03-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BOOKS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='descricao',
            field=models.CharField(max_length=4000),
        ),
    ]