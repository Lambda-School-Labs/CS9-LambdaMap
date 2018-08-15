from django.http import JsonResponse
from .models import UserProfile
from .security import encrypt_password, verify_password
import json


def str_to_bool(str):
    return str[0] == 'T' or str[0] == 't'


def create_user(request):
    if request.META['REQUEST_METHOD'] == 'POST':
        # parse the request object and pull the json object
        request_body = json.loads(request.body.decode('ascii'))
        user = UserProfile(
            username=request_body['username'],
            student=str_to_bool(request_body['student']),
            email=request_body['email'],
            pwd=encrypt_password(request_body['password'])
        )
        user.save()
        return JsonResponse(request_body, status=201)
    else:
        return JsonResponse({"Error": "incorrect request method. please make a POST request to this end point"},
                            status=400)


def log_in(request):
    if request.META['REQUEST_METHOD'] == 'POST':
        request_body = json.loads(request.body.decode('ascii'))
        user = UserProfile.objects.filter(username=request_body['username'])[0]
        return JsonResponse({"logged in": str(verify_password(request_body['password'], user.pwd))})


def delete_user(request):
    if request.META['REQUEST_METHOD'] == 'DELETE':
        request_body = json.loads(request.body.decode('ascii'))
        user = UserProfile.objects.filter(username=request_body['username'])[0].delete()
        return JsonResponse({"deleted": request_body}, status=204)