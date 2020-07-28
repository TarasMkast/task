from django.contrib import admin

from .models import History, Objtype


class BdAdmin(admin.ModelAdmin):
    list_display = ('email', 'type_object', 'published')
    list_display_links = ('email', 'published')
    search_fields = ('email', 'type_object', 'published')


admin.site.register(History, BdAdmin)
admin.site.register(Objtype)

