from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=(
            ('admin', 'admin'),
            ('teacher', 'teacher'),
            ('student', 'student'),
        ),
        default='student',
    )
    avatar = models.ImageField(blank=True, null=True)

