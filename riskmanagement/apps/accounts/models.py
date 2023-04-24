from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phone_field import PhoneField
from riskmanagement.apps.processes.models import CompanySite
from django.contrib.auth.models import PermissionsMixin

from django import template
from django.dispatch import receiver
from django.urls import reverse
from django_rest_resetpassword.signals import reset_password_token_created
from django.core.mail import send_mail  
import sys 
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


class MyAccountManager(BaseUserManager):
    
    def create_user(self, email, username, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not phone:
            raise ValueError('Users must have a phone')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name = first_name,
            last_name = last_name,
            phone = phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):
    TYPE = (
        ('I', 'Intern'),
        ('E', 'Extern'),
    )
    # Required and Essential for Custom User
    email = models.EmailField(max_length=254,verbose_name="email", unique = True)  
    username                 = models.CharField(max_length=30, unique=True)
    date_joined                = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login                = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active                = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    # Added 
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    typeUser = models.CharField(max_length=1, choices=TYPE, blank=True, null=True)
    site = models.ForeignKey (CompanySite, on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


#function that sends customized email for forgotting password

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key),
        'token' : reset_password_token.key,
        'angular_reset_password_url':"http://localhost:4200/reset-password/:" + reset_password_token.key,
    }
    template.Context({'reset_password_token.key': reset_password_token.key})
    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = "email_plaintext_message = "
    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
