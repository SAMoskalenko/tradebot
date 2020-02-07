from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    name = models.CharField(max_length=100, blank=True, null=True)
    binance_key = models.CharField(max_length=100, blank=True, null=True)
    binance_secret = models.CharField(max_length=100, blank=True, null=True)
    chat_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserAccount.objects.create(user=instance)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.name)
