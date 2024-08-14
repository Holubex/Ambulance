from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, TextField, DateField


class Profile(Model):
    # Pole pro jedinečné propojení s uživatelským modelem
    user = OneToOneField(User, on_delete=CASCADE)
    # Pole pro datum narození, volitelné
    birth_date = DateField(null=True, blank=True)

    class Meta:
        # Řazení profilů podle uživatelského jména
        ordering = ["user__username"]

    def __str__(self):
        # Reprezentace objektu Profile jako uživatelské jméno
        return f"{self.user.username}"
