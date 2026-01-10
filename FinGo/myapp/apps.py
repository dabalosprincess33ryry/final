from django.apps import AppConfig
from django.contrib.auth import get_user_model

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
    def ready(self):
        import myapp.signals  

        User = get_user_model()
        username = "admin"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email="admin@example.com",
                password="StrongPassword123"
            )
            print("Superuser created automatically.")
