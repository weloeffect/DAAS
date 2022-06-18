from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import DAAS_User
from .forms import UserLogin, UserRegister
# Create your views here.
def register(request,*args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect("home:home")
    context={}
    # if request.method == "GET":

    if request.POST:
        form = UserRegister(request.POST)
        
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            user1 = authenticate(email = email, password = raw_password)
            login(request, user1)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("home:home")
            # passwordConf = request.POST['passwordConf']
            # user = DAAS_User( first_name=first_name, last_name=last_name, phone_number = phone_number, email=email,  password = password)
            # user.save()
            # return redirect("home:home")
        else:
            context["register_form"]=form
            
    else:
        form = UserRegister()
        context['register_form'] = form
    return render(request, "html/signup.html", context)

def signin(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home:home")
    
    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))


    if request.POST:
        form = UserLogin(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                # return render(request, "html/logout.html",context)
                return redirect("home:home")
    else: 
        form = UserLogin()

    context["login_form"]=form
    return render(request, "html/login2.html", context)   
        # return render(request, "html/signin.html")

def signout(request):
    logout(request)
    # return render(request, "html/signin.html")
    return redirect("home:home")


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect

def view_profile(request):
    return render(request, "html/user_profile.html")

def edit_profile(request):
    return render(request, "html/user_edit.html")

def password_reset(request):
    return render(request, "html/password_reset-form.html")
