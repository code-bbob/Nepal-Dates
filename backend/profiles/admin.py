from django.contrib import admin
from .models import Profile,ProfileImages


class ProfileImageInline(admin.TabularInline):
    model = ProfileImages
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    inlines = [ProfileImageInline]

# Register your models here.
admin.site.register(Profile,ProfileAdmin)
