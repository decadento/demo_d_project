from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect  # noqa: disable=f401
from .forms import UserCreationForm, LoginForm, User



# Create your views here.

def index(request):
    return render(request, 'main/landing.html')

def learn(request):
    return render(request, 'main/learn.html')


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Перевірка унікальності нікнейму
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Цей нікнейм вже зайнятий. Спробуйте інший.')
            else:
                form.save()
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
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')