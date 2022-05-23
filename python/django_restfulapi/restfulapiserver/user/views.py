from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from user.models import User
from user.serializers import UserSerializer

# Create your views here.
@csrf_exempt
def user_list(request):
    """
    List all code user, or create a new user.
    """
    if request.method == "GET":
        user = User.objects.all()
        sereializer = UserSerializer(user, many=True)
        return JsonResponse(sereializer.data, safe=False)

    elif request.method == "POST":
        user = JSONParser().parse(request)
        sereializer = UserSerializer(data=user)
        if sereializer.is_valid():
            sereializer.save()
            return JsonResponse(sereializer.data, status=201)
        return JsonResponse(sereializer.errors, status=400)


@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code user.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404, content="The user does not exist.")

    if request.method == "GET":
        sereializer = UserSerializer(user)
        return JsonResponse(sereializer.data, safe=False)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        sereializer = UserSerializer(user, data=data)
        if sereializer.is_valid():
            sereializer.save()
            return JsonResponse(sereializer.data, status=201)
        return JsonResponse(sereializer.errors, status=400)

    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status=204)
