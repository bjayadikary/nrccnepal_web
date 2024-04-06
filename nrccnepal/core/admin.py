from django.contrib import admin
from .models import Contact, Programs, TestProgram, TestProgramTopic

class ProgramsAdmin(admin.ModelAdmin):
	list_filter = ('title', 'priority_in_programs', 'priority_in_home')
	list_display = ('title', 'priority_in_programs', 'priority_in_home')
	exclude = ['slug']

# Test
class TestProgramAdmin(admin.ModelAdmin):
	list_display = ('title', 'updated_datetime', 'priority_in_major_programs_list', 'priority_in_programs_list')
	list_filter = ('program_tags', 'published_date')
	exclude = ['slug']
	
class TestProgramTopicAdmin(admin.ModelAdmin):
	list_display = ('topic', 'program_title', 'topic_order')
	list_filter = ('program_title', 'topic_order')


# Register your models here.

admin.site.register(Contact)
admin.site.register(Programs, ProgramsAdmin)
admin.site.register(TestProgram, TestProgramAdmin)
admin.site.register(TestProgramTopic, TestProgramTopicAdmin)
