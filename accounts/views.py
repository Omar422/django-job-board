from django.shortcuts import render, redirect
from .forms import SignupForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse
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

def profile(request):
    form = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile_form' : form})

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_profile = profile_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            return redirect(reverse('accounts:profile'))

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    
    return render(request, 'accounts/edit_profile.html', {
        'user_form':user_form,
        'profile_form':profile_form
    })