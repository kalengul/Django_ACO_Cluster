# Generated by Django 4.1.3 on 2022-11-24 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("PG", "0001_initial"),
    ]

    operations = [
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
