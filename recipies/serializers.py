from rest_framework import serializers
from .models import Category, Recipie

class RecipieDetailSerializier(serializers.ModelSerializer):
    class Meta:
        model = Recipie
        fields = '__all__'




class RecipiesListSerializier(serializers.ModelSerializer):
    class Meta:
        model = Recipie
        fields = ('id', 'title', 'body', 'category')



class CategoryListSerializier(serializers.ModelSerializer):
    class Meta:
        model = Recipie
        fields = '__all__'



class CategoryListSerializier2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryDetailSerializier(serializers.ModelSerializer):
    class Meta:
        model = Recipie
        fields = '__all__'

