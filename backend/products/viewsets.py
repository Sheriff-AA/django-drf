from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    get -> list -> queryset
    get -> retrieve -> product instance detail view
    post -> create -> new instance
    put -> update
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"  # default
