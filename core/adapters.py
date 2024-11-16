from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        
        user_field(user, 'phone_number', data.get('phone_number'))
        user_field(user, 'card_id_number', data.get('card_id_number'))
        user_field(user, 'first_name', data.get('first_name'))
        user_field(user, 'last_name', data.get('last_name'))
        
        if commit:
            user.save()
        return user
