from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
     if request.method=='POST':
          fname=request.POST['fname']
          lname=request.POST['lname']
          email=request.POST['email']
          username=request.POST['username'] 
          password=request.POST['password']
          print(fname,lname,email,username,password)
          try:
               u=User.objects.get(username=username)
               return render(request,'register.html',{'msg':'Username already exists'})
          except:
              u=User.objects.create_user(
                   first_name=fname,
                   last_name=lname,
                   email=email,
                   username=username,
                   password=password  
          )
          # u.set_password(password)      #encrypt the password and store it in tha database
          # u.save()
     return render(request,'register.html')


def login_(request):
     if request.method=='POST':
          uname=request.POST['username']
          pswr=request.POST['password']
          print(uname,pswr)  #nitu 12345
          u=authenticate(username=uname,password=pswr) #if username and password both are correct it will return user object instance(username) else it will return None
          #next we need to login user to the application only if authenticate is returning user object instance
          if u:  #user object instance  -> true ,None -> fase
               # login the user and store the user data in session storage
               login(request,u)
               return redirect('home')
          else:
               return render(request,'login.html',{'msg':'Ivalid Credentials'})
          print(u)
     return render(request,'login.html')

@login_required(login_url='login_')
def logout_(request):
     #clear the session storage
     logout(request)
     return redirect('login_')


@login_required(login_url='login_')
def profile(request):
     return render(request,'profile.html')

@login_required(login_url='login_')
def reset(request):
     print(request.POST)
     if request.method=='POST':
          if 'old' in request.POST:
               uname=request.POST['username']
               old=request.POST['old']
               u=authenticate(username=uname,password=old)
               print(u)
               if u:
                   return render(request,'reset.html',{'new_pass':True})
               else:
                   return render(request,'reset.html',{'msg':'Incorrect old password'})
          if 'new' in request.POST:
               new=request.POST['new']
               print(new)
               u=request.user  #currently logedin user object instance
               u.set_password(new)
               u.save()
               return redirect('logout_')
     return render(request,'reset.html')

def forgot(request):
     if request.method=='POST':
          uname=request.POST['uname']
          try:
               u=User.objects.get(username=uname)
               request.session['fp_user']=u.username
               return redirect('new_password')
          except:
               return render(request,'forgot.html',{'msg':'Username does not exists'})
     return render(request,'forgot.html')

def new_password(request):
     username=request.session.get('fp_user')
     print(username)
     if not username:
          return redirect('forgot')
     user=User.objects.get(username=username)
     if request.method=='POST':
         new_pass=request.POST['new_pass']
         if user.check_password(new_pass):  #return true if new password is same as old password
              return render(request,'new.html',{'msg':'New password can not be same as old password'})
         user.set_password(new_pass)
         user.save()
         del request.session['fp_user']
         return redirect('login_')
     return render(request,'new.html')