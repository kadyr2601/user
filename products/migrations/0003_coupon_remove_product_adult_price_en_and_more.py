# Generated by Django 4.0.2 on 2022-04-30 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_alter_subcategory_parent'),
        ('products', '0002_product_about_en_product_about_ru_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=16)),
                ('is_active', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='adult_price_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='adult_price_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='children_price_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='children_price_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_price_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_price_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='partner_price_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='partner_price_ru',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_ru',
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_products', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_products', to='categories.subcategory'),
        ),
    ]
