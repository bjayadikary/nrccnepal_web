from django.contrib import admin
from .models import Contact, Programs

class ProgramsAdmin(admin.ModelAdmin):
	list_filter = ('title', 'priority_in_programs', 'priority_in_home')
	list_display = ('title', 'priority_in_programs', 'priority_in_home')
	exclude = ['slug']

# Register your models here.

admin.site.register(Contact)
admin.site.register(Programs, ProgramsAdmin)
