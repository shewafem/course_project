from rest_framework.viewsets import ModelViewSet
from category.serializers import CategorySerializer
from category.models import Category



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer