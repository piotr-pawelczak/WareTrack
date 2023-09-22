from django.contrib import admin

from waretrack.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
