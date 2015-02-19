from django.contrib import admin

# Register your models here.
from models import *


class LoggedMessageAdmin(admin.ModelAdmin):
    '''
    Custom ModelAdmin to be used for the LoggedMessage field. Enables
    filtering, searching (name and text fields), and the slick built-in
    django date-higherarchy widget.
    '''
    list_display = ('date', '__unicode__')
    list_filter = ['direction', 'date', 'identity']
    #search_fields = ['reporter__first_name', 'reporter__last_name', 'text']
    date_hierarchy = 'date'
admin.site.register(LoggedMessage, LoggedMessageAdmin)
