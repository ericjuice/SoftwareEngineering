# Generated by Django 4.1 on 2023-05-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TestTable",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=32)),
                ("test", models.DateField(auto_now_add=True)),
            ],
        ),
    ]