
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.conf import settings


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return  self.name


class Program(models.Model):
    GENERAL = "G"
    PARENTAL_GUIDANCE = "PG"
    PARENTAL_GUIDANCE_CAUTIONED = "PG-13"
    RESTRICTED = "R"
    NO_UNDER_17 = "NC-17"
    APPROPRIATE_FOR_CHILDREN_TV = "TV-Y"
    APPROPRIATE_FOR_CHILDREN_OVER_7_TV = "TV-Y7"
    SUITABLE_FOR_ALL_TV = "TV-G"
    PARENTAL_GUIDANCE_TV = "TV-PG"
    NO_UNDER_14_TV = "TV-14"
    MATURE_AUDIENCES = "TV-MA"
    NOT_RATED = "NR"

    RATINGS = [
        (GENERAL, "G"),
        (PARENTAL_GUIDANCE, "PG"),
        (PARENTAL_GUIDANCE_CAUTIONED, "PG-13"),
        (RESTRICTED, "R"),
        (NO_UNDER_17, "NC-17"),
        (APPROPRIATE_FOR_CHILDREN_TV, "TV-Y"),
        (APPROPRIATE_FOR_CHILDREN_OVER_7_TV, "TV-Y7"),
        (SUITABLE_FOR_ALL_TV, "TV-G"),
        (PARENTAL_GUIDANCE_TV, "TV-PG"),
        (NO_UNDER_14_TV, "TV-14"),
        (MATURE_AUDIENCES, "TV-MA"),
        (NOT_RATED, "NR")
    ]

    TVSHOW = "TvShow"
    MOVIE = "Movie"

    PROGRAM_TYPE = [
        (TVSHOW, "Tv Show"),
        (MOVIE, "Movie")
    ]

    title = models.CharField(max_length=250)
    yr = models.IntegerField()
    description = models.TextField()
    rating = models.CharField(max_length=10, choices=RATINGS, default=NOT_RATED)
    runtime = models.IntegerField()
    director = models.CharField(max_length=250)
    score = models.FloatField()
    program_type = models.CharField(max_length=10, choices=PROGRAM_TYPE, default=MOVIE)
    production_company = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='multi-media-animeflix')
    thumbnail = models.ImageField(upload_to='multi-media-animeflix')
    background = models.ImageField(upload_to='multi-media-animeflix')
    clip = models.FileField(upload_to='multi-media-animeflix')
    thumbclip = models.FileField(upload_to='multi-media-animeflix')
    genres = models.ManyToManyField(Genre)
    seasons = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Watchlist(models.Model):
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE
    )
    program = models.ForeignKey(
        Program, 
        on_delete=models.CASCADE
    )


class Like(models.Model):
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE
    )
    program = models.ForeignKey(
        Program, 
        on_delete=models.CASCADE
    )

    
class Dislike(models.Model):
    profile = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE
    )
    program = models.ForeignKey(
        Program, 
        on_delete=models.CASCADE
    )



















