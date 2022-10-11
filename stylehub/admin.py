from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, ClosetItem, Outfit
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "username", "bio", "profile_image",]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ClosetItem)
admin.site.register(Outfit)
