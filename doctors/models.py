from django.db import models
from accounts.models import Accounts
from patients.models import Patients
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Doctors(models.Model):
    accounts = models.OneToOneField(Accounts, on_delete = models.DO_NOTHING)
    accounts.is_doctor = True
    occupation = models.CharField(max_length = 128)
    qualification = models.CharField(max_length = 128)
    patient = models.ForeignKey(Patients, null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.accounts.first_name

@receiver(post_save, sender = Accounts)
def create_user_profile(sender, instance,created,**kwargs):
    if created:
        if instance.is_doctor:
            Doctors.objects.create(accounts = instance)
