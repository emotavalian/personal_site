from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import   CustomUserForm , CustomUserChangeForm


# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm  # For adding new users
#     form = CustomUserChangeForm        # For editing existing users
#     model = CustomUser
#     list_display = ('id','country_code','phone_number', 'full_name' , 'email', 'is_staff')

#     #for custom user change form
#     fieldsets = (
#         (None, {'fields': ('country_code','phone_number', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email', )}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

#     #for custom user add form
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('country_code', 'phone_number', 'first_name', 'last_name', 'email', 'password1','password2'),
#         }),
#     )
#     search_fields = ('phone_number', 'full_name')
#     list_filter = ('country_code', )
#     ordering = ('country_code',)
#     class Media:
#         css = {
#             'all': ('https://cdnjs.cloudflare.com/ajax/libs/select2/4.1.0-rc.0/css/select2.min.css',
#                     'admin/css/custom_admin.css',)
#         }
#         js = (
#             'https://code.jquery.com/jquery-3.6.0.min.js',
#             'https://cdnjs.cloudflare.com/ajax/libs/select2/4.1.0-rc.0/js/select2.min.js',
            
#             'admin/js/custom_admin.js',  # Your custom script
#         )




@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserForm  # Form for creating users
    form = CustomUserChangeForm 
    # fields = ('country_code', 'phone_number', 'email', 'first_name', 'last_name', 'password')
    list_display = ('id','full_name','country_code','phone_number', 'email', 'password')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    #for organizing fields into groups. user change form
    fieldsets = (
        ('Personal Info', {
            'fields': ('country_code', 'phone_number','password','first_name','last_name',  'email')
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    
    #for creating user
    add_fieldsets = (
        ('Personal Info', {
            'classes': ('wide',),
            'fields': ('phone_number', 'country_code', 'email','first_name', 'last_name', 'password', ),
        }),
    )
    search_fields = ('phone_number', 'email', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    readonly_fields = ('last_login', 'date_joined')


    

    # class Media:
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/select2/4.1.0-rc.0/css/select2.min.css',
                    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css',
                    'admin/css/custom_admin.css',)
        }
        js = (
            'admin/js/custom_admin.js',  # Your custom script
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/select2/4.1.0-rc.0/js/select2.min.js',
            
            
        )
    
    def get_form(self, request, obj = ..., change = ..., **kwargs):
        if not obj:
            kwargs['form'] = CustomUserForm
        else:
            kwargs['form'] = CustomUserChangeForm
        return super().get_form(request, obj=None, **kwargs)
    
    
    #Override the save_model method to set the password as just set_password causes to hash it
    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password'):
            obj.set_password(form.cleaned_data['password'])
        return super().save_model(request, obj, form, change)    
