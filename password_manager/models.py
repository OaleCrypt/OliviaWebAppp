from django.db import models
from .utils import fer  # Ensure this import is valid

# Example usage of the Fernet instance in the model (if needed)
class Password(models.Model):
    service = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    encrypted_password = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        # Encrypt the password before saving (optional if needed)
        self.encrypted_password = fer.encrypt(self.encrypted_password.encode()).decode()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.service} - {self.username}"



