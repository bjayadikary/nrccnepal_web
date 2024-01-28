from django.contrib import admin
from .models import Contact, Programs

class ProgramsAdmin(admin.ModelAdmin):
	exclude = ['slug']

# Register your models here.

admin.site.register(Contact)
admin.site.register(Programs, ProgramsAdmin)
