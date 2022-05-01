from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category')
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
