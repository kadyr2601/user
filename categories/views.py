from rest_framework import generics
from rest_framework.decorators import APIView
from categories.models import Category, SubCategory
from categories.serializers import CategorySerializer, CategoryListENSerializer, CategoryListRUSerializer, \
    SubCategorySerializer, SubCategoryCreateSerializer


class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CategoryListRU(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListRUSerializer


class CategoryListEN(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListENSerializer


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoryCreate(generics.CreateAPIView):
    serializer_class = SubCategoryCreateSerializer


class SubCategoryList(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class SubCategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()
