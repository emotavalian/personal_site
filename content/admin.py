from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'edited_at', 'category')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

