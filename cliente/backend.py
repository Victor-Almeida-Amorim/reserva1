from django.contrib.auth.backends import BaseBackend
from .models import Cliente

class ClienteBackend(BaseBackend):
    def authenticate(request, email, password):
        try:
            cliente = Cliente.objects.get(email=email)
            if cliente.senha == password:
                return cliente
        except Cliente.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Cliente.objects.get(pk=user_id)
        except Cliente.DoesNotExist:
            return None
