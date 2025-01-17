from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserInfoUpdate, ProfilePicUpdate
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'title': 'Sign Up'
    }
    
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserInfoUpdate(request.POST, instance=request.user)
        p_form = ProfilePicUpdate(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Account information updated successfully')
            return redirect('profile')
        
    else:
        u_form = UserInfoUpdate(instance=request.user)
        p_form = ProfilePicUpdate(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

def userProfile(request, username):
    user_details = Profile.objects.get(user=request.user)
    return render(request, 'users/userProfile.html', {'user_details':user_details})