# Create your models here.


from django.db import models
import jwt

from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
        AbstractBaseUser, BaseUserManager , PermissionsMixin
    )

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self,email, username ,mi, firstname, lastname, password):

        if username is None:
            raise TypeError("Username cannot be left blank")

        if firstname is None:
            raise TypeError("Users first name cannot be left blank")

        if lastname is None:
            raise TypeError("Users last name cannot be left blank")

        if password is None:
            raise TypeError("Users password cannot be left blank")

        if email is None:
            raise TypeError("Users need an email")


        user = self.model(
            username = username , mi = mi,firstname = firstname, lastname = lastname, email = self.normalize_email(email)
        )

        user.set_password(password)

        user.save()

        return  user

    def create_superuser(self,email, username,mi ,firstname, lastname, password):

        user = self.create_user(email,username,mi,firstname,lastname,password)

        user.is_superuser = True

        user.is_staff = True

        user.save()

        return user


class User( AbstractBaseUser, PermissionsMixin):

    username = models.CharField(db_index = True , max_length = 255, unique = True)

    firstname = models.CharField(max_length = 75, default = "N/A")

    lastname = models.CharField(max_length = 100, default = "N/A")

    email = models.EmailField( db_index = True , unique = True)

    is_active = models.BooleanField(default = True)

    is_staff = models.BooleanField(default = False)

    created_at = models.DateTimeField(auto_now_add = True)

    updated_at = models.DateTimeField(auto_now = True)

    USERNAME_FIELD  = 'email'

    REQUIRED_FIELDS = ['username','firstname','lastname']

    objects =UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        """
        generates a JSON web token that stores the users id and has an
        expiary date set to 60 days into the future
        """

        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

