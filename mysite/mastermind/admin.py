from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created')
    inlines = [CommentInline]
    readonly_fields = ('created',)
    list_filter = ('author','created',)
    search_fields = ('title', 'content', 'author__username')


    fieldsets = [
        ('General', {'fields': ('title', 'content', 'author', 'created')})
    ]


# Register your models here.
admin.site.register(Post, PostAdmin)
