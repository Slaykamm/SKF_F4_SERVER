from django.shortcuts import render
from rest_framework import generics
from recipies.serializers import CategoryListSerializier, RecipieDetailSerializier, RecipiesListSerializier, CategoryDetailSerializier, CategoryListSerializier2
from recipies.models import Recipie, Category
from rest_framework import viewsets

# Create your views here.

class CreateRecipieView(generics.CreateAPIView):
    serializer_class = RecipieDetailSerializier


class RecipieListView(generics.ListAPIView):
    serializer_class = RecipiesListSerializier
    queryset = Recipie.objects.all()


class RecipieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipieDetailSerializier
    queryset = Recipie.objects.all()



class CategoryListView2(generics.ListAPIView):
      serializer_class = CategoryListSerializier2
      queryset = Category.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializier
    queryset = Recipie.objects.all()




class CategoryListView(viewsets.ModelViewSet):
   queryset = Recipie.objects.all()
   serializer_class = CategoryListSerializier



   def get_queryset(self, **kwargs):
        id =  self.request.query_params.get('id', None)
        category =  self.request.query_params.get('category', None)
        name =  self.request.query_params.get('name', None)        
        print("test otsyuda")

        if category:
            return Recipie.objects.filter(category=category)

        elif name:
            return Recipie.objects.filter(name=name)

        elif id:
            return Recipie.objects.filter(id=id)
            
        else:
            return Recipie.objects.all()
