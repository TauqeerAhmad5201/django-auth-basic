# from this import d
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, request 
# from django.contrib.auth.models import User
# from django.contrib import messages
# from accounts.models import CustomUser
# from django.contrib import redirects
# from django.contrib.auth import authenticate, login,logout

# # Create your views here.
# def index(request):
#     return render(request,'index.html')

# def join(request):
#     return render(request,'join.html')

# def signup(request):
#     return render(request,'signup.html')

# def signupsent(request):
#     if request.method == 'POST':
#         firstname = request.POST['fname']
#         height = request.POST['height']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
        
#         if password1==password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already registered.')
#                 return redirect('/signup')
#             else:
#                 ins = User.objects.create_user(email, password1,height)
#                 ins.save()

#                 # myuser = User.objects.create_user(username = username,firstname=firstname, lastname=lastname,email=email, password1=password1, password2=password2)
#         # myuser.first_name = firstname
#         # myuser.last_name = lastname 
#                 # myuser.save()
#                 messages.success(request, "Welcome ! Your Account Created !")
#                 return redirect('/account')
        
#         else:
#             print('Passwords not matching.')

#     else:
#         return HttpResponse('404- USE POST')

# def loginsent(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password'] 
#         print(email,password)
#         user = authenticate(request,email = email, password1 = password)
#         print(user)
#         if user is not None:
#             login(request,user)
#             messages.success(request,'Successfully Logged In as {email}')
#         else:
#             messages.error(request,'Sorry ! Invalid Credentials')
#             # return HttpResponse('login failed')
#             return redirect('/account')
#     else:
#         return HttpResponse('HAVE POST !')

# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'