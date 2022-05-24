from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from argon2 import PasswordHasher

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
        user["password"] = PasswordHasher().hash(user["password"])
        sereializer = UserSerializer(data=user)

        try:
            if User.objects.get(name=user["name"]):
                return HttpResponse(status=404, content="The user already exist.")
        except:
            pass

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
        data["password"] = PasswordHasher().hash(data["password"])
        sereializer = UserSerializer(user, data=data)

        if sereializer.is_valid():
            sereializer.save()
            return JsonResponse(sereializer.data, status=201)
        return JsonResponse(sereializer.errors, status=400)

    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status=204)


@csrf_exempt
def login(request):
    """
    Login User
    """
    if request.method == "POST":
        login_user = request.POST.get("userid", "")
        login_password = request.POST.get("userpw", "")
        # print(login_user, login_password)

        try:
            password = User.objects.get(name=login_user).password
        except User.DoesNotExist:
            return HttpResponse(status=404, content="The user does not exist.")

        try:
            if PasswordHasher().verify(password, login_password):
                # print("로그인 성공~")
                return JsonResponse({"code": "0000", "msg": "로그인성공입니다."}, status=200)
        except:
            # print("로그인 실패ㅜㅠㅜ")
            return JsonResponse({"code": "1001", "msg": "로그인실패입니다."}, status=401)

    return render(request, "user/login.html")
