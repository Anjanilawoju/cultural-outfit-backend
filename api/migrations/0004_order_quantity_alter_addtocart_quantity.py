# Generated by Django 5.0.1 on 2024-09-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_order_addtocart_rating_addtocart_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="addtocart",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
