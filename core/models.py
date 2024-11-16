from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import ValidationError , EmailValidator
from .managers import CustomUserManager

def phone_number_validator(self):
        
        if len(self) != 11 or not self.isdigit() or self[0] != '0':
            raise ValidationError("please enter a valid phone number")
        
        return self

def name_validator(self ):
        
        if not self.isalpha():
            raise ValidationError(" name must be alphabetic")
        return self
    


class CustomUser(AbstractUser):
    username = None  # Remove username field
    phone_number = models.CharField(validators=[phone_number_validator],unique=True, max_length=11, )
    email = models.EmailField(validators=[EmailValidator],null=True, blank=True)
    otp_code = models.PositiveSmallIntegerField(null=True, blank=True)
    otp_code_created = models.DateTimeField(auto_now_add=True)
    
    first_name = models.CharField(max_length=255, validators=[name_validator], blank=True,)
    last_name = models.CharField(max_length=255, validators=[name_validator], blank=True,)
    
    # card_id_number = models.CharField(unique=True, max_length=10,blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    backend = "core.backends.PhoneNumberBackend"