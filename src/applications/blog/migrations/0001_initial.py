from django.db import migrations
from django.db import models

import applications.blog.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(blank=True, null=True, unique=True)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "created_at",
                    models.DateTimeField(default=applications.blog.models._now),
                ),
                ("nr_likes", models.IntegerField(default=0)),
            ],
        ),
    ]
