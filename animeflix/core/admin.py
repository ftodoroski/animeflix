from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


# admin.site.site_header = 'Chase'

admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Program)
admin.site.register(models.Dislike)
admin.site.register(models.Like)
admin.site.register(models.Watchlist)
admin.site.register(models.Genre)
# admin.site.register(models.P)
