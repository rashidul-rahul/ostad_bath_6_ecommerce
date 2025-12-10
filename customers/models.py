import datetime
import uuid
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='customer'
    )
    test_field = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user.first_name:
            return f"{self.user.first_name} {self.user.last_name}"
        return self.user.username

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class ResetPassword(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='password_token'
    )
    token = models.CharField(max_length=120, default=uuid.uuid4)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token

    def is_valid(self):
        if self.is_used:
            return False
        exp_time = self.created_at + datetime.timedelta(hours=1)
        if self.created_at < exp_time:
            return True

        return False
