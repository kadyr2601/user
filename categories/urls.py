from django.urls import path
from categories.views import CategoryCreate, CategoryListRU, CategoryListEN, CategoryDetails,\
                            SubCategoryCreate, SubCategoryList, SubCategoryDetails


urlpatterns = [
    path('category/create/', CategoryCreate.as_view()),
    path('category/list/ru/', CategoryListRU.as_view()),
    path('category/list/en/', CategoryListEN.as_view()),
    path('category/update/<pk>/', CategoryDetails.as_view()),
    path('sub-category/create/', SubCategoryCreate.as_view()),
    path('sub-category/list/', SubCategoryList.as_view()),
    path('sub-category/update/<pk>/', SubCategoryDetails.as_view()),
]
