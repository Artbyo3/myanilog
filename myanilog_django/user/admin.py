from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class UserProfileAdmin(UserAdmin):

    list_display = ('username', 'email', 'first_name',
                    'last_name', 'bio', 'birth_date', 'created_at')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'birth_date', 'profile_picture', )}),
    )
    readonly_fields = ('created_at',)


# search_fields = ('username', 'email', 'first_name', 'last_name')
# list_filter = ('is_staff', 'is_active')
admin.site.register(UserProfile, UserProfileAdmin)
