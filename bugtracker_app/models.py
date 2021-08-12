from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class CustomUserModel(AbstractUser):
    role_choices = (
            ('Admin', 'Admin'),
            ('Dev', 'Dev'),
            ('Boss Man', 'Boss Man')
    )
    role = models.CharField(
            max_length=60,
            choices=role_choices,
            null=True,
            blank=True)


class Tickets(models.Model):
    status_choices = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    )
    title = models.CharField(max_length=120)
    submit_time = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=500)
    filed_by = models.ForeignKey(
            CustomUserModel,
            related_name='filed_by_CustomUser',
            null=True,
            on_delete=models.SET_NULL
            )
    status = models.CharField(
            max_length=30,
            choices=status_choices
            )
    assigned_to = models.ForeignKey(
            CustomUserModel,
            related_name='assigned_to_CustomUser',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            default=None
            )
    completed_by = models.ForeignKey(
            CustomUserModel,
            related_name='completed_by_CustomUser',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            default=None
            )
