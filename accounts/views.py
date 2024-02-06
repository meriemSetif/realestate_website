from pprint import pprint
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, f"this username: {username} is already taken!")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f"this email: {email} is already taken!")
                    return redirect("register")
                else:
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    # auth.login(request,user)
                    user.save()
                    messages.success(request, f"user {user} created successfully!")
                    return redirect("login")

        else:
            messages.error(request, "the passwords doesn't match")
            return redirect("register")
    return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        username_given = request.POST.get("username", "")
        password_given = request.POST.get("password", "")
        print(f"the current user is:{username_given}")
        print(f"with password:{password_given}")
        user = auth.authenticate(
            request, username=username_given, password=password_given
        )
        if user is not None:
            print(f"user has been authenticated:")
            pprint(user)
            auth.login(request, user)
            messages.success(
                request, f"successfully logged in !\nWelcome back {username_given}"
            )
            return redirect("dashboard")
        else:
            messages.error(request, f"invalid credentials!")
            return redirect("login")
    return render(request, "accounts/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, f"you've logged-out successfully!")
        return redirect("index")
    return redirect("index")


def dashboard(request):

    contacts = Contact.objects.order_by("-contact_date").filter(user=request.user)
    print("the retrieved contacts are:")
    pprint(contacts)
    context = {"contacts": contacts}
    return render(request, "accounts/dashboard.html", context)
