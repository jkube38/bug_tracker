from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bugtracker_app.models import CustomUserModel, Tickets


# Register your models here.
UserAdmin.fieldsets += ('Role', {'fields': ('role',)}),
admin.site.register(CustomUserModel, UserAdmin)
admin.site.register(Tickets)
