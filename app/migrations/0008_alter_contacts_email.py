# Generated by Django 4.2 on 2023-04-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0007_remove_education_month"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacts",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Эл.почта*"),
        ),
    ]
