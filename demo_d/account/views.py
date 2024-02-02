from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect  # noqa: disable=f401
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .forms import SignUpForm
from .forms import UpdateProfileForm
from account.models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'main/landing.html')

def learn(request):
    return render(request, 'main/learn.html')

def admin(request):
    return render(request,'admin.html')

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    template_name = 'account/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'account/profile.html'


class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'account/profile.html'
    context_object_name = 'user'


def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=request.user.id)
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'account/update_profile.html', {'form': form})