# Generated by Django 4.2 on 2023-04-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_alter_contacts_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="cv",
            name="status",
            field=models.CharField(
                choices=[("ACTIVE", "Активна"), ("NOT_ACTIVE", "Неактивна")],
                default="NOT_ACTIVE",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
    ]
