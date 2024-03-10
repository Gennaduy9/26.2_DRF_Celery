# Generated by Django 5.0.3 on 2024-03-09 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_alter_coursesubscription_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursesubscription",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to="courses.course",
                verbose_name="Курс",
            ),
        ),
    ]
