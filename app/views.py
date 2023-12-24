from django.shortcuts import render
from django.http import JsonResponse
import json
from uuid import uuid4
from .models import Customer

# Create your views here.

def index(req):
    return render(req, 'index.html', {})

# def signin(req):
#     if req.method == 'POST':
#         data = json.loads(req.body)
#         print(data)
#         try:
#             Customer.objects.get(email=data['email'], password=data['password'])
#             return JsonResponse({'status' : 200})
#         except Exception as e:
#             print(e)
#         return JsonResponse({'status' : 304})
#     return render(req, 'signin.html', {})

# def signup(req):
#     if req.method == 'POST':
#         data = json.loads(req.body)
#         try:
#             if not Customer.objects.filter(email = data['email']).exists():
#                 cus_obj = Customer(uuid4().hex, data['name'], data['email'], data['password'])
#                 cus_obj.save()
#                 return JsonResponse({'status' : 200})
#             else:
#                 return JsonResponse({'status' : 300})
#         except Exception as e:
#             print(e)
#         return JsonResponse({'status' : 400})
#     return render(req, 'signup.html', {})