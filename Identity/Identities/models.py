# Create  models for Identities app.

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

from django.contrib.auth.models import User


# Create your models here.

class UserManager(BaseUserManager):

	# Create a model manager for User model with no user name field


	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):

		# Create and save a User with the given email and password

		if not email:

			raise ValueError('The given email must be set')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_user(self, email, password=None, **extra_fields):

		# Create and save a regular User with the given email and password.

		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):

		# Create and save a SuperUser with the given email and password.

		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

	# User Model

	username = None
	email = models.EmailField(_('email address '), unique = True)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()



class UserProfile(models.Model):

	user = models.OneToOneField(User)
	contact = models.IntegerField(default=0)


def create_profile(sender, **kwargs):

	if kwargs['created']:

		user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender = User )
