from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import User


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'bio', 'email',
                  'role',)


class UserAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'username', 'bio',
                    'email', 'role',)


admin.site.register(User, UserAdmin)
