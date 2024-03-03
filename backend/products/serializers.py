from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title
from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.HyperlinkedIdentityField(
        view_name="product-update",
        lookup_field="pk",
    )
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = [
            "owner",
            "url",
            "update_url",
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "public",
        ]

    # def validate_title(self, value):
    #     request = self.context.get("request")
    #     user= request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")

    #     return value

    def get_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_update_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)

    def get_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()
