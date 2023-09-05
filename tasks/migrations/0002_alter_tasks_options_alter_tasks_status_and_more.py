# Generated by Django 4.0 on 2023-09-04 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_options_alter_users_mail'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ('-date_creation',), 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('В ожидании', 'В ожидании'), ('В процессе', 'В процессе'), ('Завершено', 'Завершено')], default='В ожидании', max_length=11),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='users.users'),
        ),
    ]
