# Generated by Django 3.1.4 on 2020-12-04 16:10

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post", options={"ordering": ["-created_at"]}
        ),
    ]
