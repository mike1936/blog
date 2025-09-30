from django.contrib import admin
from .models import Post, Category, Tag, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'published_at', 'created_at']
    list_filter = ['status', 'category', 'tags', 'created_at', 'published_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    date_hierarchy = 'published_at'
    ordering = ['-created_at']

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'status')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'featured_image')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Meta', {
            'fields': ('published_at',),
            'classes': ('collapse',)
        })
    )

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'post', 'created_at', 'is_approved']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['author_name', 'author_email', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Mark selected comments as approved"
