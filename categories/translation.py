from modeltranslation.translator import register, TranslationOptions
from categories.models import Category, SubCategory


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
