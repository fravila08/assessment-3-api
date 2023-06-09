# Generated by Django 4.1.7 on 2023-03-19 06:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import ecom_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0005_remove_cartitem_cart_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True, validators=[ecom_app.validators.validate_acceptable_categories])),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='genre',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.99, max_digits=10, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=10)]),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom_app.category'),
        ),
    ]
