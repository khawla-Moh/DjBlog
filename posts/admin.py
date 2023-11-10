from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post,Category,Comments



class ProductAdmin (SummernoteModelAdmin):
    list_display=['title','category','draft']
    list_filter=['draft','tags']
    search_fields=['title','tags']
    summernote_fields = ('content',)




admin.site.register(Post,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comments)

