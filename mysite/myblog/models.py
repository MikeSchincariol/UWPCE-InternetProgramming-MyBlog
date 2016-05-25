from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(
        Post,
        blank=True,
        related_name='categories'
    )

    def __str__(self):
        return self.name




class CategoryPostInline(admin.StackedInline):
    model = Category.posts.through


class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
    list_display = ("name", "description")
    inlines = [CategoryPostInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_date", "published_date")
    list_filter = ("title", "categories__name")
    inlines = [CategoryPostInline]