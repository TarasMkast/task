from django.contrib import admin

from findplace.models import History


class BdAdmin(admin.ModelAdmin):
    list_display = ('email', 'type_object', 'published')
    list_display_links = ('email', 'published')
    search_fields = ('email', 'type_object', 'published')


admin.site.register(History, BdAdmin)
