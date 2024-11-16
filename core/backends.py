from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class PhoneNumberBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        
        UserModel = get_user_model()

        # Try to fetch user by phone number first, if it's numeric, otherwise by email
        try:
            if username.isnumeric():
                user = UserModel.objects.get(phone_number=username)
            else:
                user = UserModel.objects.get(email=username)
                
            if user.check_password(password):
                
                return user
        except UserModel.DoesNotExist:
           
            return None
        return None
    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

#