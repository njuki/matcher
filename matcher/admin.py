# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *


class CompaniesAdmin(admin.ModelAdmin):
    """
    Companies admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Companies, CompaniesAdmin)

class IndustriesAdmin(admin.ModelAdmin):
    """
    Industries admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Industries, IndustriesAdmin)

class UsersAdmin(admin.ModelAdmin):
    """
    Users admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Users, UsersAdmin)

class JobTypesAdmin(admin.ModelAdmin):
    """
    JobTypes admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(JobTypes, JobTypesAdmin)

class JobsAdmin(admin.ModelAdmin):
    """
    Jobs admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Jobs, JobsAdmin)

class QualificationParametersAdmin(admin.ModelAdmin):
    """
    QualificationParameters admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(QualificationParameters, QualificationParametersAdmin)

class JobQualificationParametersAdmin(admin.ModelAdmin):
    """
    JobQualificationParameters admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(JobQualificationParameters, JobQualificationParametersAdmin)

class JobSeekersAdmin(admin.ModelAdmin):
    """
    JobSeekers admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(JobSeekers, JobSeekersAdmin)

class SeekersQualificationParametersAdmin(admin.ModelAdmin):
    """
    SeekersQualificationParameters admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(SeekersQualificationParameters, SeekersQualificationParametersAdmin)

class ChannelsAdmin(admin.ModelAdmin):
    """
    Channels admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Channels, ChannelsAdmin)

class OutMessagesAdmin(admin.ModelAdmin):
    """
    OutMessages admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(OutMessages, OutMessagesAdmin)

class JobApplicantMatchesAdmin(admin.ModelAdmin):
    """
    JobApplicantMatches admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(JobApplicantMatches, JobApplicantMatchesAdmin)

class InboxAdmin(admin.ModelAdmin):
    """
    Inbox admin class
    """
    # search_fields = ('name', 'id')
    # list_filter = ('creation_date','modification_date') 
    # list_display = ('id', 'name')
    pass

admin.site.register(Inbox, InboxAdmin)


admin.site.register(Education)
admin.site.register(Skillset)
