from django.contrib import admin

from .models import UserProfile # tutorial


from .models import Grant
from .models import Project
from .models import Airport
from .models import Sponsor
from .models import Report

# #class ProjectsInline(admin.TabularInline):
#     model = Project 

# class ProjectAdmin(admin.ModelAdmin):
#   fields = ['project_description']

# class GrantAdmin(admin.ModelAdmin):
#   fields = ('grant_number', 'grant_amount')
#   inlines = [ProjectsInline]

# class AirportAdmin(admin.ModelAdmin):
#     fields = ['airport_name',      'airport_locid']
# #    list_displays = ('airport_name', 'airport_locid')
# #    fieldsets = [
# #        (None,  {'fields': ['airport_name']}),
# #        ('Airport LOCID', {'fields': ['airport_locid']}),

# class SponsorAdmin(admin.ModelAdmin):
#     fields = ['sponsor_name']
# #    ]
admin.site.register(UserProfile) # added for tutorial
admin.site.site_header = 'AIP Administration'
admin.site.site_title = "AIP"
admin.site.index_title = "FAA ATL-ADO"

admin.site.register(Airport)
admin.site.register(Project)
admin.site.register(Grant)
admin.site.register(Sponsor)
admin.site.register(Report)
