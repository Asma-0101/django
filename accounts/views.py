from django.shortcuts import render, redirect
from django.contrib.auth import get_user, authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                username = form.cleaned_data['username']
                request.session['username'] = username
                return redirect('/crudapp/')
            except Exception as e:
                if 'username' in str(e):  # Check if username is the duplicate field
                    messages.error(request, 'Username already exists.')
                    return redirect('/accounts/login_user')
                else:
                    messages.error(request, 'An error occurred during registration.')  # Generic error for other integrity issues
                    return redirect('/accounts/login_user')
        else:
            messages.error(request, form.errors)  # Display form validation errors
            return redirect('/accounts/login_user')
    else:
        form = RegistrationForm()
        return render(request, 'authentication/register.html', {'form':form})
                                       
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('/crudapp/')
        else:
            messages.success(request, "Oops! Could not login you in, please try again :)")
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})
    

def logout_user(request):
    logout(request)
    return redirect('login')