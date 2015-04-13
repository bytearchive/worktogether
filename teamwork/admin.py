from django.contrib import admin

from .models import TeamMember, WorkDone


class WorkDoneAdmin(admin.ModelAdmin):

    list_display = ['date', 'person']

admin.site.register(TeamMember)
admin.site.register(WorkDone, WorkDoneAdmin)
