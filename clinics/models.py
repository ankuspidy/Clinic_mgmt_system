from django.db import models
from accounts.models import Accounts
from patients.models import Patients
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Clinics(models.Model):
    accounts = models.OneToOneField(Accounts, on_delete = models.DO_NOTHING)
    accounts.is_clinic_admin = True
    clinic_patient_relation = models.ForeignKey(Patients, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.accounts.first_name

@receiver(post_save, sender = Accounts)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if(instance.is_clinic_admin):
            Clinics.objects.create(accounts = instance)
