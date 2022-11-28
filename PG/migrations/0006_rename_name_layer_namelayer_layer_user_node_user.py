# Generated by Django 4.1.3 on 2022-11-24 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("PG", "0005_rename_namelayer_layer_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="layer",
            old_name="name",
            new_name="NameLayer",
        ),
        migrations.AddField(
            model_name="layer",
            name="User",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="node",
            name="User",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
            preserve_default=False,
        ),
    ]
