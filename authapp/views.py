from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Contact, MembershipPlan, Trainer, Enrollment
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
            messages.info(request, "Por favor digitalize 9 digitos")
            return redirect('/signup')

        if pass1 != pass2:
            messages.info(request, "Senha não funcional")
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.warning(request, "Numero De Telefone obtido")
                return redirect('/signup')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email obtido")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, "Cadastro bem sucedido!")
        return redirect('/login')

    return render(request, "signup.html")


def validarlogin(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login bem sucedido")
            return redirect('/')
        else:
            messages.error(request, "Credenciais Invalidas...")
            return redirect('/login')

    return render(request, "validarlogin.html")


def validarlogout(request):
    logout(request)
    messages.success(request, "Saiu da conta com sucesso!")
    return redirect('/login')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('fullName')
        email = request.POST.get('email')
        number = request.POST.get('num')
        desc = request.POST.get('desc')
        myquery = Contact(name=name, email=email,
                          phonenumber=number, description=desc)
        myquery.save()

        messages.info(request, "Thanks for Contacting us we will get you soon")
        return redirect('/contact')

    return render(request, "contact.html")


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Por favor, é necessario fazer o Login")
        return redirect('/login')

    membership = MembershipPlan.objects.all()
    selectTrainer = Trainer.objects.all()
    context = {"membership": membership, "selectTrainer": selectTrainer, }
    if request.method == "POST":
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phoneNumber = request.POST.get('phoneNumber')
        dob = request.POST.get('dob')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        reference = request.POST.get('reference')
        address = request.POST.get('address')
        query = Enrollment(fullName=fullName, email=email, gender=gender, phoneNumber=phoneNumber,
                           dob=dob, selectMembershipPlan=member, selectTrainer=trainer, reference=reference, address=address)
        query.save()
        messages.success(request, " Matrícula bem sucedida!")
        return redirect('/join')

    return render(request, "enroll.html", context)
