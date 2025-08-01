# Generated by Django 5.2.4 on 2025-07-19 21:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarian',
            name='library',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='relationship_app.library'),
        ),
        migrations.AlterField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(to='relationship_app.book'),
        ),
        migrations.AlterField(
            model_name='library',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
