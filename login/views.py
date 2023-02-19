from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import SigninForm,SignupForm

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'User '+ user +' successfully added')
            redirect('login/signup')
    context = {'register_form':form}
    return render(request, "login/signup.html", context)


def signin_view(request):
    if request.method == "POST":
        form = SigninForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = SigninForm()
    return render(request, "login/signin.html", context={"login_form": form})


def signout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("../login")
