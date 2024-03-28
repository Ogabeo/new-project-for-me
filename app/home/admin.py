from django.contrib import admin
from .models import Tags, Category, New, About, Contact, Ads



class CategoryAdmin(admin.ModelAdmin):
    list_display=("id", "name" )
    list_display_links=("id", "name")
    prepopulated_fields={"slug": ['name']}
 
class NewAdmin(admin.ModelAdmin):
    list_display=("id", "author", "title", "category" )
    list_display_links=("id", "title", )
    prepopulated_fields={"slug": ['title']}
    readonly_fields=("views", )
    filter_horizontal=("tags", )
    list_editable=("category", "author", )
# Register your models here.

admin.site.register(Tags)
admin.site.register(About)
admin.site.register(Contact)


class AdsAdmin(admin.ModelAdmin):
    list_display=("id", "link", "position", "is_active")
    list_editable=("is_active", "position")

admin.site.register(Category, CategoryAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Ads, AdsAdmin)





