from django.contrib import admin
from django.urls import path
from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """Returns a list of URLs for the Django admin site, including additional URLs for managing user authentication.

    Returns:
        list: A list of URLs for the Django admin site.
    """

    list_display = ("id", "email", "username", "is_staff", "is_superuser", "is_active")
    list_display_links = ("email", "username")

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "user/",
                self.admin_site.admin_view(self.changelist_view),
                name="auth_user_changelist",
            ),
            path(
                "user/add/",
                self.admin_site.admin_view(self.add_view),
                name="auth_user_add",
            ),
            path(
                "user/<int:id>/change/",
                self.admin_site.admin_view(self.change_view),
                name="auth_user_change",
            ),
            path(
                "user/<int:id>/delete/",
                self.admin_site.admin_view(self.delete_view),
                name="auth_user_delete",
            ),
        ]
        return my_urls + urls


admin.site.register(CustomUser, CustomUserAdmin)
