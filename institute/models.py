from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    family_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    sex = models.BooleanField(null=True)
    date_of_birth = models.DateTimeField(null=True)
    nationality = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)
    mobile_number = models.CharField(max_length=100, null=True)
    introduction = models.CharField(max_length=100, null=True)
    fields_of_interest  = models.CharField(max_length=100, null=True)
    name_of_company_or_organization = models.CharField(max_length=100, null=True)
    industry_name = models.CharField(max_length=100, null=True)
    your_position = models.CharField(max_length=100, null=True)
    name_of_the_institute_you_took_the_mba_emba = models.CharField(max_length=100, null=True)
    course = models.BooleanField(null=True)
    member = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class GeneralDegreeInfo(models.Model):
    school = models.CharField(max_length=100, null=True)
    graduated = models.BooleanField(null=True)
    faculty = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    completion_status = models.BooleanField(null=True)
    year_of_entered = models.IntegerField(null=True)
    year_of_graduation = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    
class MbaInfo(models.Model):
    school = models.CharField(max_length=100, null=True)
    graduated = models.BooleanField(null=True)
    faculty = models.CharField(max_length=100, null=True)
    department = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    completion_status = models.BooleanField(null=True)
    year_of_entered = models.IntegerField(null=True)
    year_of_graduation = models.IntegerField(null=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
