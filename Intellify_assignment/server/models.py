from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    def create_user(self,
                    user_name,
                    user_id,
                    user_phone,
                    user_email,
                    user_display_name,
                    password=None):
        if not user_name:
            raise ValueError('Users must have an user name')
        elif not user_id:
            raise ValueError('Users must have an user id')
        elif not user_phone:
            raise ValueError('Users must have an user phone')
        elif not user_email:
            raise ValueError('Users must have an email')
        elif not user_display_name:
            raise ValueError('Users must have an user display name')
        user = self.model(
            user_id=user_id,
            user_name=user_name,
            user_email=self.normalize_email(user_email),
            user_phone=user_phone,
            user_display_name=user_display_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, user_id, user_phone, user_email,
                         user_display_name, password):

        user = self.create_user(user_id=user_id,
                                user_name=user_name,
                                user_email=self.normalize_email(user_email),
                                user_phone=user_phone,
                                user_display_name=user_display_name,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(
        max_length=128,
        verbose_name='UserId', 
        unique=True,   
    )
    user_name = models.CharField(max_length=120,
                                 verbose_name="Username",
                                 unique=True)
    user_phone = models.CharField(
        max_length=31,
        verbose_name="Phone",
    )
    user_display_name = models.CharField(max_length=60, verbose_name='Name')
    user_email = models.EmailField(
        verbose_name='Email',
        max_length=255,
    )
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = [
        'user_id', 'user_phone', 'user_display_name', 'user_email'
    ]

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def generate_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)