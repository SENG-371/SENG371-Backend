# Generated by Django 4.1.7 on 2023-04-03 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_practitioner_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="practitioner",
            name="password",
            field=models.CharField(
                default="pbkdf2_sha256$390000$3R2bajC0Ktm6HYi4RUeFGG$WSJay8YpTK4s9pRfLgv5OxRX8oemICwVkFQIVYKNqyg=",
                help_text="Required. Must be set.",
                max_length=128,
                verbose_name="password",
            ),
        ),
    ]
