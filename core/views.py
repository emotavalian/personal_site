from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from allauth.account.views import SignupView
from django.views import View


def home_page_view(request):
    return render(request, 'core/home.html')


def about_page_view(request):
    return render(request, 'core/contact_us.html')


def contact_page_view(request):
    return render(request, 'core/about_us.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser

class CustomLoginView(View):
    template_name = 'account/login.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        identifier = request.POST.get('login')
        password = request.POST.get('password')
        
        try:
            # Check if user exists with this phone number or email
            user = CustomUser.objects.get(phone_number=identifier)
        except CustomUser.DoesNotExist:
            try:
                user = CustomUser.objects.get(email=identifier)
            except CustomUser.DoesNotExist:
                return render(request, self.template_name, {'error': 'User not found'})
        
        # Verify password
        if user.check_password(password):
            login(request, user)
            return redirect('home')
        
        return render(request, self.template_name, {'error': 'Invalid password'})


