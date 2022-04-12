from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    """A model manager with no username field."""

    use_in_migrations = True

    def get_queryset(self):
        """Return user queryset."""
        return super().get_queryset()

    def _create_user(self, email, password, **extra_fields):
        """Create and Save a User with given email and password."""
        if not email:  # pragma no cover
            raise ValueError("email must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("username", email)
        # extra_fields.setdefault('confirmed_at', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password.""" ""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("username", email)
        extra_fields.setdefault("utype", "ADMINISTRATOR")
        if extra_fields.get("is_staff") is not True:  # pragma no cover
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:  # pragma no cover
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """A User."""

    class Types:
        """User Types Enum."""

        STUDENT = "STUDENT", "STUDENT"
        LIBRARIAN = "LIBRARIAN", "LIBRARIAN"
        ADMINISTRATOR = "ADMINISTRATOR", "ADMINISTRATOR"
        choices = (
            STUDENT,
            LIBRARIAN,
            ADMINISTRATOR,
        )

    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.CharField(
        max_length=40,
        unique=True,
        primary_key=True,
    )
    utype = models.CharField(
        "Type",
        max_length=50,
        choices=Types.choices,
        default="LIBRARIAN",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = UserManager()

    @property
    def is_librarian(self):
        return self.utype != "STUDENT"

    def __str__(self):
        """Return string repr."""
        return self.email + "\t" + self.first_name + "\t" + self.last_name


class StudentsManager(models.Manager):
    """Students Manager."""

    def get_queryset(self, *args, **kwargs):
        """Return students queryset."""
        return super().get_queryset(*args, **kwargs)


class Student(models.Model):
    """Student User."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library_card_number = models.CharField(
        max_length=40,
        unique=True,
        blank=True,
    )
    objects = StudentsManager()

    def __str__(self):
        """Return string representation."""
        return self.library_card_number + "\t" + str(self.user)

    class Meta:
        """Meta class."""
