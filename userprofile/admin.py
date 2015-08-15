from django.contrib import admin
from .models import UserProfile, Achievement, Redeem


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Achievement)
admin.site.register(Redeem)