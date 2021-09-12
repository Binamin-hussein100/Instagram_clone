from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1=request.POST['password']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                print('already exists')    
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.add_message(request, messages.warning,'Email already exists! Try another.')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,email=email,password=password1)
                    user.save()
                    return redirect('login')
        else:
            messages.add_message(request,messages.warning,'Password must match!')
            return redirect('register')
    else:
        return render(request,'registration.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        
        user = auth.authenticate(username = username,password = password)
        
        if user is not None:
            auth.login(request,user)
            print('Login successfull!')
            return redirect('instagram')
        else:
            print('invalid credencials!')
            return redirect('login')
    
    else:
        return render(request,'login.html')
        
                    