# Generated by Django 4.2 on 2023-04-19 18:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_alter_contacts_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacts",
            name="phone",
            field=models.CharField(
                blank=True, max_length=30, verbose_name="Номер телефона*"
            ),
        ),
    ]