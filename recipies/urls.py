from django.contrib import admin
from django.urls import path, include
from recipies.views import *

urlpatterns = [
    path('recipie/create', CreateRecipieView.as_view()),
    path('all/', RecipieListView.as_view()),
    path('recipie/detail/<int:pk>/', RecipieDetailView.as_view()),
    path('category/all', CategoryListView2.as_view()),
 #   path('category/<int:pk>/', CategoryDetailView.as_view()),

]
