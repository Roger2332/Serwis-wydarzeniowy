from django.contrib.auth.models import AbstractUser
from django.db import models


class CreateUserModel(AbstractUser):
    ROLE_CHOICES = [
        ('organizator', 'Organizator'),
        ('zwykly', 'Zwykły użytkownik')
    ]

    rola = models.CharField(choices=ROLE_CHOICES, max_length=50, default=ROLE_CHOICES[1][0])
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)


class CreateWydarzenieModel(models.Model):
    title = models.CharField(max_length=100, null=False)
    deta_open = models.DateField(null=False)
    deta_close = models.DateField(null=False)
    description = models.TextField(null=False)
    user_append = models.ForeignKey(CreateUserModel, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f""""
        TYTUL:  {self.title}
        DETA:  {self.deta_open} - {self.deta_close}
        OPIS:   {self.description}
        UZYTKOWNIK:     {self.user_append}
        """
