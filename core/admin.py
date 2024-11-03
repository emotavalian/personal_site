from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
   list_display = ("username", "email","card_id_number")
   # for adding id_card_number to change form admin
   fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email","card_id_number")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
   # # for adding id_card_number to add form admin
   add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1","password2", "email","first_name","last_name","card_id_number"),
            },
        ),
    )
