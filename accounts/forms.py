from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Perfil


class PerfilCreationForm(UserCreationForm):
    class Meta:
        model = Perfil
        fields = ("username", "email")

    # (opcional) estilos base si quieres
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ["username", "email", "password1", "password2"]:
            if name in self.fields:
                self.fields[name].widget.attrs.update({"class": "form-control"})


class PerfilChangeForm(UserChangeForm):
    # oculta el campo password hash del UserChangeForm
    password = None

    class Meta:
        model = Perfil
        # ✅ declara explícitamente lo que quieres editar
        fields = (
            "username",
            "first_name", "last_name",
            "email",
            # si tu modelo Perfil tiene estos, los puedes ir agregando:
            # "pais", "fecha_de_nacimiento", "direccion", "avatar",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # (opcional) vuelve email obligatorio
        if "email" in self.fields:
            self.fields["email"].required = True

        # (opcional) estilos base
        for f in self.fields.values():
            # file inputs (avatar) también quedan con form-control
            f.widget.attrs.update({"class": "form-control"})
