import phonenumbers
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import ValidationError , EmailValidator, RegexValidator
from phonenumber_field.modelfields import PhoneNumberField, validate_international_phonenumber
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE, parse, is_valid_number, NumberParseException
from phonenumbers import format_number, PhoneNumberFormat
from .managers import CustomUserManager
   
def name_validator(self ):
        
        if not self.isalpha():
            raise ValidationError(" name must be alphabetic")
        return self
    
class CustomUser(AbstractUser):
    CHOICES_CODE_COUNTRY=[(f"{code}", f"{code}, {region[0]}") for code, region in COUNTRY_CODE_TO_REGION_CODE.items()]
    username = None  # Remove username field
    
    phone_number = models.CharField( max_length=18,unique=True )
    country_code = models.CharField(max_length=4, blank=True, null=True, choices=CHOICES_CODE_COUNTRY, default=+98)
    email = models.EmailField(validators=[EmailValidator],null=True, blank=True)
    otp_code = models.PositiveSmallIntegerField(null=True, blank=True)
    otp_code_created = models.DateTimeField(auto_now_add=True)
    
    first_name = models.CharField(max_length=255, validators=[name_validator], blank=True,)
    last_name = models.CharField(max_length=255, validators=[name_validator], blank=True,)
    
        
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    backend = "core.backends.PhoneNumberBackend"

    def __str__(self):
        # Convert phone_number to a string
        return f"{self.first_name} : {str(self.phone_number)}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    def clean(self):
        country_code = self.country_code
        
        raw_number = self.phone_number.strip().lstrip('0')
        
        if not raw_number.startswith('+') :
            full_number = f'+{country_code}{raw_number}'
        else:
            full_number = raw_number  
        try:
            phone_number_parsed= parse(full_number, None)
          
            if  is_valid_number(phone_number_parsed):
                 self.phone_number = format_number(phone_number_parsed, PhoneNumberFormat.E164)
            else:
                raise ValidationError("Invalid phone number format")
        except NumberParseException as e:
            raise ValidationError("Invalid phone number: {e}")

        super().clean()
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)       
                