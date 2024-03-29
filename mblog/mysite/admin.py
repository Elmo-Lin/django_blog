from django.contrib import admin
from mysite.models import Post, NewTable, Product
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
admin.site.register(Post, PostAdmin)
admin.site.register(NewTable)
admin.site.register(Product)