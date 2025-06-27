from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.TextField()
    sex = models.CharField(max_length=10)
    
class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

class UserEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()

class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credits = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    offer_used = models.CharField(max_length=255)

class Bin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    t_num = models.IntegerField()
    dry_waste = models.IntegerField()
    wet_waste = models.IntegerField()
    e_waste = models.IntegerField()

class DryWaste(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

class WetWaste(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

class EWaste(models.Model):
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

class Truck(models.Model):
    t_num = models.IntegerField(primary_key=True)
    t_time = models.TimeField()
    t_date = models.DateField()
    m_phn_no = models.CharField(max_length=15)

class TruckLocation(models.Model):
    t_num = models.ForeignKey(Truck, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

class Carries(models.Model):
    t_num = models.ForeignKey(Truck, on_delete=models.CASCADE)
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)

class MEmployee(models.Model):
    m_phn_no = models.CharField(primary_key=True, max_length=15)
    m_name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    m_sex = models.CharField(max_length=10)
    m_salary = models.DecimalField(max_digits=10, decimal_places=2)

class MEmployeeEmail(models.Model):
    m_employee = models.ForeignKey(MEmployee, on_delete=models.CASCADE)
    email = models.EmailField()
