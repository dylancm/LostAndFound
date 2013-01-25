from django.contrib import admin
from landf.models import Object


class ObjAdmin(admin.ModelAdmin):
    list_display = ['title', 'when', 'recently_lost_found']
    list_filter = ['when']
    search_fields = ['title']
    date_heirarchy = 'when'

admin.site.register(Object, ObjAdmin)
