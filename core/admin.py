from django.contrib import admin
from . import models


class FolderAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['name',]
    list_display =['name',]
    list_filter = ('name',)
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("name",)}

    class Meta:
        model= models.Folder

class DivisionAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['heading',]
    list_display =['heading','slug',"small_description",]
    list_filter = ('heading',)
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("heading",)}

    class Meta:
        model= models.Division

class DownloadAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['file_name',]
    list_display =['category','file_name',]
    list_filter = ('file_name','category',)
    readonly_fields = ['updated','timestamp']

    class Meta:
        model= models.Download

class BlogPostAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['title',]
    list_display =['title','slug',]
    list_filter = ('title',)
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("title",)}

    class Meta:
        model= models.BlogPost

class VacancyAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['job_type','job_title',]
    list_display =['job_title','slug',]
    list_filter = ('job_title',)
    readonly_fields = ['updated','timestamp']
    prepopulated_fields = {"slug":("job_title",)}

    class Meta:
        model= models.Vacancy


class EmblemAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['name','file_size',]
    list_display =['name','file_size','link',]
    list_filter = ('name',)
    readonly_fields = ['updated','timestamp','file_size']

    class Meta:
        model= models.Emblem

class TenderAdmin(admin.ModelAdmin):
    date_hierarchy='timestamp'
    search_fields =['name','file_size',]
    list_display =['name','file_size','due_date','time','active']
    list_filter = ('name',)
    readonly_fields = ['updated','timestamp','file_size']

    class Meta:
        model= models.Tender






# Register your models here.
admin.site.register(models.Slider)
admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.Folder,FolderAdmin)
admin.site.register(models.Division,DivisionAdmin)
admin.site.register(models.Image)
admin.site.register(models.Team)
admin.site.register(models.Media)
admin.site.register(models.Legislation)
admin.site.register(models.LegislationFile)
admin.site.register(models.Download, DownloadAdmin)
admin.site.register(models.Vacancy, VacancyAdmin)
admin.site.register(models.Emblem, EmblemAdmin)
admin.site.register(models.Tender, TenderAdmin)
