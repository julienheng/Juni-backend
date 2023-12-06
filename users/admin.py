from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["email", "name",
                    "is_active", "is_staff",]
    list_display_links = ["email"]
    list_filter = ["email", "name", 'userType',
                   "is_active"]
    search_fields = ["email", "name", 'userType',]
    fieldsets = (
        (
            _("Login Credentials"), {
                "fields": ("email", "password",)
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": ('name', 'userType', "is_active",)
            },
        ),
        # (
        #     _("Permissions and Groups"),
        #     {
        #         "fields": ("is_staff", "is_superuser", "groups", "user_permissions")
        #     },
        # ),
        (
            _("Important Dates"),
            {
                "fields": ("last_login",)
            },
        ),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "name", 'userType', "password1", "password2", "is_active"),
        },),
    )


admin.site.register(User, UserAdmin)
