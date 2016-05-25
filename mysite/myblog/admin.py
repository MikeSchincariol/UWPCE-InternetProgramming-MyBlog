from django.contrib import admin

from myblog.models import Category, CategoryAdmin
from myblog.models import Post, PostAdmin


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
