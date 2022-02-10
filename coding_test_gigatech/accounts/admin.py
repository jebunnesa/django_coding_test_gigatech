from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from .models import CustomUser, CustomGroup
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry, CHANGE
from django.db.models import Q
from django.utils.safestring import mark_safe


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'contact_number', 'is_active', 'is_staff',
                    'is_superuser')
    exclude = ('last_modified_by', 'created_by')
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'contact_number', 'username', 'password',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_joined', 'last_login', )}),
    )
    list_filter = ('is_superuser', 'groups__name')
    search_fields = ('username',)

    def save_model(self, request, obj, form, change):
        if change:
            obj.last_modified_by = request.user
        else:
            obj.is_staff = True
            obj.created_by = request.user
            obj.last_modified_by = request.user

        if 'password' in form.changed_data:
            obj.set_password(obj.password)
            obj.save()
        else:
            pass

        super(CustomUserAdmin, self).save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)


class CustomGroupAdmin(GroupAdmin):
    list_display = ('name',)
    exclude = ('last_modified_by', 'created_by')

    def save_model(self, request, obj, form, change):
        if change:
            obj.last_modified_by = request.user
        else:
            obj.created_by = request.user
            obj.last_modified_by = request.user
        super(CustomGroupAdmin, self).save_model(request, obj, form, change)


admin.site.unregister(Group)
admin.site.register(CustomGroup, CustomGroupAdmin)