from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField('first_name', max_length=35)
    last_name = models.CharField('last_name', max_length=35)
    phone_number = models.CharField(
        max_length=12,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(12)
        ]
    )
    email = models.EmailField(db_index=True, unique=True)
    image = models.FileField(upload_to='profile_images/', default='/media/samples/sample.jpeg')

    def __str__(self) -> str:
        return f"User({self.email})"