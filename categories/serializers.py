from rest_framework import serializers
from categories.models import Category, SubCategory
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'
        depth = 1


class SubCategoryRUSerializer(serializers.ModelSerializer):
    sub_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name_ru', 'sub_products']


class SubCategoryENSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name_en']


class CategoryListRUSerializer(serializers.ModelSerializer):
    sub_category = SubCategoryRUSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name_ru', 'sub_category']


class CategoryListENSerializer(serializers.ModelSerializer):
    sub_category = SubCategoryENSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name_en', 'sub_category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryCreateSerializer(serializers.ModelSerializer):
    parent = CategorySerializer(many=True)

    class Meta:
        model = SubCategory
        fields = '__all__'
