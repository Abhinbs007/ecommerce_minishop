from django.contrib import admin
from.models import *
# Register your models here.

class pro(admin.ModelAdmin):
    list_display =['name','slug','img','desc','stock','price','date','category']
    list_editable = ['img','desc','stock','price','date','category']
    prepopulated_fields = {'slug': ('name',)}

class cats(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}






admin.site.register(cate,cats)
admin.site.register(product,pro)





