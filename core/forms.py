from django import forms
from allauth.account.forms import SignupForm, LoginForm
from allauth.account.adapter import get_adapter
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from .models import CustomUser

class CustomSignupForm(SignupForm):
    card_id_number = forms.CharField(max_length=10,required=False,)
    phone_number = forms.CharField(max_length=11, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    field_order = ['phone_number', 'email', 'card_id_number', 'first_name', 'last_name', 'password1']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        #check if phone number is already registered
        if len(phone) != 11 or not phone.isdigit() or phone[0] != '0':
            raise forms.ValidationError("please enter a valid phone number")
        if CustomUser.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError("This phone number is already registered")
        return phone

    def clean_first_name(self):
        first_name=self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("First name must be alphabetic")
        return first_name
    
    def clean_last_name(self):
        last_name=self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must be alphabetic")
        return last_name
    
    def save(self, request):
        adapter = get_adapter() # Get the allauth adapter
        user = adapter.new_user(request)   # Create a new user instance but don’t save it yet
        adapter.save_user(request, user, self) # save new user to the database based on default data in allauth adapter
        self.custom_signup(request, user) #s an allauth hook you can use to add more customization to the signup process. This method is empty by default, so you’d only need to add this if you want to further customize the user’s setup.
       
        # custom_signup is an allauth hook uses to add more customization to the signup process. This method is 
        # empty by default, just ueses for further customize the user’s setup.
        self.custom_signup(request, user) #s an allauth hook you can use to add more customization to the signup process. This method is empty by default, so you’d only need to add this if you want to further customize the user’s setup.
        
        user.phone_number = self.cleaned_data['phone_number'] #add extra data to the user
        user.card_id_number = self.cleaned_data['card_id_number']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        
        return user





class CustomLoginForm(LoginForm):
    login = forms.CharField(label="Email or Phone Number")
    
    def clean_login(self):
        login = self.cleaned_data['login']
        # Allow login with either email or phone number
        return login

    def login(self, request, redirect_url=None):
        user = self.user
        auth_login(request, user)
        return user





