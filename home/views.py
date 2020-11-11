from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def handleSignup(request):
    if request.method == 'POST' and request.FILES:
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pic = request.FILES['pic']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname 
        myuser.last_name = lname 
        myuser.profile_pic = pic
        myuser.save()
        return redirect('handleSignup')
    return render(request, 'signup.html')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return redirect('handleSignup')
    return render(request, 'login.html')

def panel(request):
    return render(request, 'panel.html')