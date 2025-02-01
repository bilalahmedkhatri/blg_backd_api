from django.contrib import admin
from .models import Category, Tag, Post, UploadedImage, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'count')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'count')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'status', 'created_at', 'updated_at')


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at', 'uploaded_by', 'status', 'notification_sent')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # List display configuration
    list_display = (
        'email', 
        'first_name',
        'last_name',
        'is_verified',
        'is_approved',
        'is_active',
        'is_staff',
        'created_at',
        'last_login'
    )
    
    # Filter options
    list_filter = (
        'is_verified',
        'is_approved',
        'is_active',
        'is_staff',
        'is_superuser',
        'groups'
    )
    
    # Search fields
    search_fields = ('email', 'first_name', 'last_name')
    
    # Ordering
    ordering = ('-created_at',)
    
    # Read-only fields
    readonly_fields = (
        'created_at',
        'last_login',
        'date_joined'
    )
    
    # Fieldset organization
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {
            'fields': (
                'first_name',
                'last_name'
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_verified',
                'is_approved',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ),
        }),
        (_('Important Dates'), {
            'fields': (
                'last_login',
                'date_joined',
                'created_at'
            )
        }),
    )
    
    # Add user fields
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name'
            ),
        }),
    )
    
    # Bulk actions
    actions = [
        'approve_users',
        'reject_users',
        'activate_users',
        'deactivate_users'
    ]

    def activate_users(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} users activated")

    def deactivate_users(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} users deactivated")

    def approve_users(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} users approved")

    def reject_users(self, request, queryset):
        updated = queryset.update(is_approved=False)
        self.message_user(request, f"{updated} users rejected")
