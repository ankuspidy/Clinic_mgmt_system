from django.db import models



# Create your models here.
class Accounts(models.Model):
    first_name = models.CharField(max_length = 55)
    last_name = models.CharField(max_length = 55)
    email = models.EmailField()
    password = models.CharField(max_length = 128)
    confirm_password = models.CharField(max_length = 128)
    is_doctor = models.BooleanField(default = False,null = True,blank = True)
    is_patient = models.BooleanField(default = False,null = True,blank = True)
    is_busines_admin = models.BooleanField(default = False, null = True, blank = True)
    is_clinic_admin = models.BooleanField(default= False, null = True, blank = True)
    joining_date = models.DateField(auto_now = True)

    def __str__(self):
        return self.first_name
