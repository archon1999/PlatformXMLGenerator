# Generated by Django 3.2 on 2021-10-17 04:34

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20211017_0927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelManagers(
            name='project',
            managers=[
                ('projects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='backend.user'),
            preserve_default=False,
        ),
    ]