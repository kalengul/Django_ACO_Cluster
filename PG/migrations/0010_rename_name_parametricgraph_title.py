# Generated by Django 4.1.3 on 2022-11-24 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("PG", "0009_remove_layer_node_remove_parametricgraph_layer_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="parametricgraph",
            old_name="name",
            new_name="title",
        ),
    ]