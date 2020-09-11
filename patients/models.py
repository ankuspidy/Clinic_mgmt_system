from django.db import models
from accounts.models import Accounts
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Patients(models.Model):
    account = models.OneToOneField(Accounts, on_delete = models.CASCADE)
    account.is_patient = True
    

    def __str__(self):
        return self.account.first_name


@receiver(post_save, sender = Accounts)
def create_user_profile(sender, instance,created,**kwargs):
    if created:
        if(instance.is_patient):
            Patients.objects.create(account = instance)
