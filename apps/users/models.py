from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, alias, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not alias:
            raise ValueError("Alias is required")
        email = self.normalize_email(email)
        user = self.model(email=email, alias=alias, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, alias, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, alias, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    alias = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["alias"]

    class Meta:
        db_table = "users"
        ordering = ["-created_at"]

    def __str__(self):
        return f"@{self.alias}"