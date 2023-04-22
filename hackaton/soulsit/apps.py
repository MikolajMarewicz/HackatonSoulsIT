from django.apps import AppConfig


class SoulsitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'soulsit'


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import soulsit.signals