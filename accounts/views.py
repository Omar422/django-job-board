from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login
# Create your views here.

def signup(request):
    
    if request.method == "POST":
        account_form = SignupForm(request.POST)
        if account_form.is_valid():
            # save new user data in db
            account_form.save()
            user_name = account_form.cleaned_data['username']
            user_pass = account_form.cleaned_data['password1']
            # check if user and pass exist to login the new user => change session
            user = authenticate(username = user_name, password = user_pass)
            login(request, user)

            return redirect('/accounts/profile')

    else:
        account_form = SignupForm()
    
    return render(request, 'registration/signup.html', {'form':account_form})