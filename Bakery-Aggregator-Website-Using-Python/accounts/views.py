
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect


class SignUpView(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'signup.html'

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('list')  # Redirect to the desired page after logout