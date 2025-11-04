# accounts/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# ✅ Mantiene compatibilidad con la migración antigua
def avatar_upload_to(instance, filename):
    username = getattr(getattr(instance, "user", None), "username", "anon")
    return f"avatars/{username}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    pais = models.CharField(max_length=50, blank=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to=avatar_upload_to, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

# ✅ crea el perfil automáticamente al crear el usuario
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)
