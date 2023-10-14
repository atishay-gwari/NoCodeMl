from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
from django.contrib.auth.decorators import login_required


def Home(request):
    return render(request, "home.html")



# Login and Signup

def signuppage(request):
    if request.method == "POST":
        user = request.POST["Name"]
        e_mail = request.POST["email"]
        password1 = request.POST["password"]
        confirmpassword = request.POST["confirmpassword"]

        if password1 == confirmpassword:
            if not User.objects.filter(username=user).exists():

                if not User.objects.filter(email=e_mail).exists():

                    user = User.objects.create_user(
                        username=user, email=e_mail, password=password1
                    )
                    user.save()
                    # messages.success(request, "Account Created!")
        return redirect("login")
    return render(request, "signup.html")


def loginpage(request):
    if request.method == "POST":
        username = request.POST["Name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # pruser)
            login(request, user)
            return redirect("home")
        # premail,password)
        else:
            # messages.error(request, "Error please check your credentials!")
            return redirect("login")
    else:
        return render(request, "login.html")


@login_required(login_url="login")
def logoutpage(request):
    # pr"logout")
    logout(request)
    return redirect("home")
