from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # يمكنك إضافة حقول إضافية لاحقًا مثل phone_number أو avatar
    pass
