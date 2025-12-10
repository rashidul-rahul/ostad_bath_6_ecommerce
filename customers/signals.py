from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from customers.models import Customer
from django.contrib.auth.models import User

from allauth.account.signals import user_signed_up

import time


@receiver(pre_save, sender=Customer)
def before_product_save(sender, instance, **kwargs):
    if not instance.test_field:
        instance.test_field = "abc"

    # time.sleep(5)
    print(f"Pre save: Customer Going to be updated, user:{instance.user.id}, Customer:{instance.id}")


# New Customer Going to be crated!!, None


@receiver(post_save, sender=Customer)
def after_save_customer(sender, instance, created, **kwargs):
    if created:
        print("New customer created:", instance.id)
    else:
        print("Customer updated:", instance.id)


# Pre save: Customer Going to be updated, user:7, Customer:None
# New customer created: 6


# Pre save: Customer Going to be updated, user:7, Customer:6
# Customer updated: 6


@receiver(user_signed_up)
def create_customer_from_allauth(request, user, **kwargs):
    Customer.objects.create(user=user)
