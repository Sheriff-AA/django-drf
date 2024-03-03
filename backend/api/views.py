import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwrargs):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        print(serializer)
        data = serializer.data
        return Response(data)

    # /**
    # GETTING DATA USING DRF and Serializers

    # instance = Product.objects.all().order_by("?").first()
    # data = {}

    # if instance:
    #      data = ProductSerializer(instance).data

    # return Response(data)
    # **/

    # /**
    # Using basic django JSON response

    # if model_data:

    #     data = model_to_dict(model_data, fields=['id', 'title', 'price'])

    #     # /*
    #     # data['id'] = model_data.id
    #     # data['title'] = model_data.title
    #     # data['content'] = model_data.content
    #     # data['price'] = model_data.price
    #     # **/

    # return JsonResponse(data)
    # **/

    # .................

    # /**
    # BASIC HTTP request with python

    # body = request.body
    # data = {}

    # try:
    #     data = json.loads(body)
    # except:
    #     pass

    # print(data)
    # data["headers"] = dict(request.headers)
    # data["params"] = dict(request.GET)
    # data["content_type"] = request.content_type
    # return JsonResponse(data)
    # **/
