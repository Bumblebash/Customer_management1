from django.apps import AppConfig


class CustomerManagement1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CRM1'
    
    def ready(self):
        import CRM1.signals
