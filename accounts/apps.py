from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        """
        Performs initialization tasks when the application is ready.

        Args:
            self: The instance of the application.

        Raises:
            None.

        Returns:
            None."""

        import accounts.signals
