from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def Home(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username) > 9 or len(username) < 9:
            messages.info(request, "Phone Number Must be 9 Digits")
            return redirect('/signup')

        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('/signup')

        try:
            if User.object.get(username=username):
                messages.warning(request, "Phone Number is Taken")
                return redirect('/signup')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email is Taken")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "User is Created Login")
        return redirect('/login')

    return render(request, "signup.html")


def validarlogin(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Sucessful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credenciais...")
            return redirect('/login')

    return render(request, "validarlogin.html")


def validarlogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/login')
