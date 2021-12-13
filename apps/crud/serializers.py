from rest_framework import serializers
from apps.pos.models import Category


# category api serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_id', 'category_name')
