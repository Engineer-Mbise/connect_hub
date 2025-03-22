from django.contrib import admin
from .models import Discussion,Module

# Register your models here.

class ModuleAdmin(admin.ModelAdmin):
    list_display=["name","description"]
    
    
class DiscussionAdmin(admin.ModelAdmin):
    list_display=["module","created_at","jitsi_meet_url","is_live"]
    

admin.site.register(Module, ModuleAdmin)
admin.site.register(Discussion, DiscussionAdmin)


