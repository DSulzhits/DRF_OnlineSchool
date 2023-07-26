from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as UserBaseManager
from django.apps import apps


class UserManager(UserBaseManager):
    """Command to create user or superuser"""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        email = GlobalUserModel.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("For superuser, value is_staff must be True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("For superuser, value is_superuser must be True")

        return self._create_user(email, password, **extra_fields)
