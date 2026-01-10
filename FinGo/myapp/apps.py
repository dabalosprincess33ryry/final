import os
from django.apps import AppConfig
from django.contrib.auth import get_user_model

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        import myapp.signals  # Keep your signals import

        # Only create superuser if CREATE_SUPERUSER is set
        if os.getenv("CREATE_SUPERUSER") != "1":
            return

        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not username or not password:
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            print("✅ Superuser created")
