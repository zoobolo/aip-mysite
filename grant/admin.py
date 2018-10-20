from django.contrib import admin

from .models import UserProfile # tutorial


from .models import Grant
from .models import Project
from .models import Airport
from .models import Sponsor
from .models import Report

class ProjectsInline(admin.TabularInline):
    model = Project 

class AirportsInline(admin.StackedInline):
    model = Airport
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets  = [
        (None,           {'fields': ['grant']}),
        ('Project Description', {'fields': ['project_description']}), 
    ]
#    fields = ['grant','project_description']
#    list_displays = ('grant', 'project_description')
    
#    inlines = [ProjectsInline]

class GrantAdmin(admin.ModelAdmin):
    fields = ['grant_number', 'grant_amount','airport']
#    inlines = [ProjectsInline]
    
class AirportAdmin(admin.ModelAdmin):
    # field = ['airport_name', 'airport_locid', 'ado_pm']
    # list_displays = ('airport_name', 'airport_locid', 'ado_pm')
    fieldsets = [
        (None,           {'fields': ['airport_name']}),
        ('Airport Data', {'fields': ['airport_locid']}), 
        ('Airport PM',   {'fields': ['ado_pm'], 'classes': ['collapse']}),
    ]
#    inlines = [AirportsInline]


class SponsorAdmin(admin.ModelAdmin):
    fields = ['sponsor_name', 'sponsor_type']
#    list_displays = ('sponsor_name','sponsor_type','sponsor_addr1',
        # 'sponsor_addr2','sponsor_addr3','sponsor_city','sponsor_state',
        # 'sponsor_zip','sponsor_county','sponsor_DUN','sponsor_ADO')
    
admin.site.register(UserProfile) # added for tutorial
admin.site.site_header = 'AIP Administration'
admin.site.site_title = "AIP"
admin.site.index_title = "FAA ATL-ADO"

admin.site.register(Airport, AirportAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Grant, GrantAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Report)
