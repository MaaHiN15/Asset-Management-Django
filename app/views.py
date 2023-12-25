from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse
from .models import *

# Create your views here.

def index(req):
    return render(req, 'index.html', {})

def userList(req):
    return render(req, 'userlist.html', {})

def userAdd(req):
    try:
        if req.method == "POST":
            return JsonResponse({'status': 200, 'text' : 'User Created Successfully!!!'})
    except Exception as e:
        return JsonResponse({'status': 400, 'text' : e})
    return render(req, 'useradd.html', {})

def userEdit(req):
    pass

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