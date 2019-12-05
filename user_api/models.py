from django.db import models
from django.contrib.auth.models import BaseUserManager, \
                                        PermissionsMixin, AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import get_user_model

# User = get_user_model()
class UserManager(BaseUserManager):

    def create_user(self, email, password = None, **extra_feilds):
        #create & save new user
        if not email:
            raise ValueError('Users must have email')
        user = self.model(email = self.normalize_email(email), **extra_feilds)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password):
        '''Create and save superuser'''
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True

class User(AbstractUser, PermissionsMixin):
    """user nodel which uses email instead of username"""
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = True) 
    is_staff = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return "{}".format(self.email)