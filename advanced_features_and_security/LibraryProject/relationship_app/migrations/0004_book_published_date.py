# Generated by Django 5.2.4 on 2025-07-25 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_alter_book_options_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
