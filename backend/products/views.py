from rest_framework import generics, mixins
from django.shortcuts import get_object_or_404
from django.http import Http404

from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin, UserQuerysetMixin

from .models import Product
from .serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    UserQuerysetMixin,
    generics.ListCreateAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # print(serializer)
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None

        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     return qs.filter(user=request.user)


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ProductDetailAPIView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(
    StaffEditorPermissionMixin,
    generics.ListAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")

        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.create(self, *args, **kwargs)


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        # get request -> detail view or list view
        # url_args?

        if pk is not None:
            # Detail View
            # queryset = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data

            return Response(data)
        else:
            # LIST VIEW
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data

            return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            print(serializer)
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None

            if content is None:
                content = title
            serializer.save(content=content)

            return Response(serializer.data)
