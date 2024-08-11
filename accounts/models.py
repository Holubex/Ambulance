from django.contrib.auth.models import User as DjangoUser
from django.db.models import Model, OneToOneField, CASCADE, TextField, DateField


class Profile(Model):
    django_user = OneToOneField(DjangoUser, on_delete=CASCADE)
    birth_date = DateField(null=True, blank=True)

    class Meta:
        ordering = ["django_user__username"]

    def __str__(self):
        return f"{self.django_user.username}"
