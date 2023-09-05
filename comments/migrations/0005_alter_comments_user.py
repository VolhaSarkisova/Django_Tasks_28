# Generated by Django 4.0 on 2023-09-05 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_options_alter_users_mail'),
        ('comments', '0004_alter_comments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to='users.users'),
        ),
    ]
