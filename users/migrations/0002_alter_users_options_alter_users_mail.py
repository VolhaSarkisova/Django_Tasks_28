# Generated by Django 4.0 on 2023-09-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('login',), 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='users',
            name='mail',
            field=models.EmailField(help_text='Enter a user email', max_length=254, verbose_name='User email'),
        ),
    ]
