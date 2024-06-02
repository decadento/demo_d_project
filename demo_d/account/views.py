from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect  # noqa: disable=f401
from .forms import UserCreationForm, LoginForm, User
from django.contrib import messages


# Create your views here.

def landing(request):
    return render(request, 'main/landing.html')

def learn(request):
    return render(request, 'main/learn.html')

def fpv(request):
    return render(request, 'account/fpv.html')

def turniket(request):
    return render(request, 'account/turniket.html')

def at4(request):
    return render(request, 'account/at4.html')

def m2a2(request):
    return render(request, 'account/m2a2.html')

def osint(request):
    return render(request, 'account/osint.html')

def emergency_pack(request):
    return render(request, 'account/emergency_pack.html')


def landing_eng(request):
    return render(request, 'main/landing_eng.html')

def learn_eng(request):
    return render(request, 'main/learn_eng.html')

def fpv_eng(request):
    return render(request, 'account/fpv_eng.html')

def turniket_eng(request):
    return render(request, 'account/turniket_eng.html')


def at4_eng(request):
    return render(request, 'account/at4_eng.html')

def m2a2_eng(request):
    return render(request, 'account/m2a2_eng.html')

def osint_eng(request):
    return render(request, 'account/osint_eng.html')

def emergency_pack_eng(request):
    return render(request, 'account/emergency_pack_eng.html')


# signup page




def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Цей нікнейм вже зайнятий. Спробуйте інший.')
            elif password1 != password2:
                form.add_error('password2', 'Паролі не співпадають.')
            else:
                form.save()
                messages.success(request, 'Ви успішно зареєструвалися. Тепер увійдіть у свій акаунт.')
                return redirect('login')
    else:
        form = UserCreationForm()   
    return render(request, 'account/signup.html', {'form': form})




# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('landing')
            else:
                form.add_error(None, 'Wrong username or password!')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('landing')

def user_signup_eng(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            # Check the uniqueness of the username
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Цей нікнейм вже зайнятий. Спробуйте інший.')
            # Check if passwords match
            elif password1 != password2:
                form.add_error('password2', 'Паролі не співпадають.')
            else:
                form.save()
                messages.success(request, 'Ви успішно зареєструвалися. Тепер увійдіть у свій акаунт.')
                return redirect('login_eng')
    else:
        form = UserCreationForm()
    
    return render(request, 'account/signup_eng.html', {'form': form})




# login page
def user_login_eng(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('landing_eng')
            else:
                form.add_error(None, 'Wrong username or password!')
    else:
        form = LoginForm()

    return render(request, 'account/login_eng.html', {'form': form})

# logout page
def user_logout_eng(request):
    logout(request)
    return redirect('landing_eng')