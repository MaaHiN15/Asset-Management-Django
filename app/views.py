from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import *
import json

# Create your views here.

def index(req):
    return render(req, 'index.html', {})

def userList(req):
    return render(req, 'userlist.html', {'users' : User.objects.all()})

def userAdd(req):
    try:
        if req.method == "POST":
            data = json.loads(req.body.decode("utf-8"))
            if data['id'] != None:
                User.objects.filter(id=data['id']).update(emp_no=data['emp_no'], name=data['name'], email=data['email'], phone_no=data['phone'])
                return JsonResponse({'status': 303})
            user = User.objects.create(emp_no=data['emp_no'], name=data['name'], email=data['email'], phone_no=data['phone'], password=data['password'])
            user.save()
            return JsonResponse({'status': 200, 'text' : 'User Created Successfully!!!'})
    except Exception as e:
        return JsonResponse({'status': 400, 'text' : e})
    return render(req, 'useradd.html', {})

def userEdit(req):
    id = req.GET.get('id')
    return render(req, 'useradd.html', {'edituser' : True, 'user' : User.objects.filter(id=id).values()[0]})

def userDelete(req):
    User.objects.filter(id=req.GET.get('id')).delete()
    return redirect(reverse('userList'))

def labelList(req):
    return render(req, 'label.html', {'label' : req.GET.get('label'), 'labels' : Label.objects.all()})

def labelAdd(req):
    if req.method == 'POST':
        name = req.POST.get('labelName')
        if not Label.objects.filter(name=name).exists():
            label = Label.objects.create(name=name)
            label.save()
            return redirect(reverse('labelList')+'?label=True')
        return redirect(reverse('labelList')+'?label=False')
    

def labelDelete(req):
    Label.objects.filter(id=req.GET.get('id')).delete()
    return redirect(reverse('labelList')+'?label=Delete')

def stockList(req):
    pass

def stockAdd(req):
    pass

def stockEdit(req):
    pass

def billList(req):
    pass

def billAdd(req):
    pass

def billEdit(req):
    pass



 


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