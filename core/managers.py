from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number=None, email=None, password=None, **other_fields):
        if not phone_number and not email:
            raise ValueError("Either phone number or email must be provided")
        if email:
            email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number=None, email=None, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        return self.create_user(phone_number, email, password, **other_fields)



