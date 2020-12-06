from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20201204_1910"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="title",
        ),
        migrations.AddField(
            model_name="post",
            name="edited",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="post",
            name="nr_views",
            field=models.IntegerField(default=0),
        ),
    ]
