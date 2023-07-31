from django.contrib import admin

from . import models #from this folder import models

# Register your models here.
# define what models can be displayed by the admin
class NotesAdmin(admin.ModelAdmin):
    # pass #no additional config on this admin model
    list_display = ('title',)

admin.site.register(models.Notes, NotesAdmin)

