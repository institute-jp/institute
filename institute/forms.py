from django import forms
from . import models
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
class CreateMember(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = [
                "full_name", 
                "family_name", 
                "first_name", 
                "gender", 
                "date_of_birth", 
                "nationality", 
                "address", 
                "phone_number", 
                "mobile_number",
                "introduction",
                "fields_of_interest",
                "name_of_company_or_organization",
                "industry_name",
                "your_position",
                "name_of_the_institute_you_took_the_mba_emba",
                "course",
                ]

class GeneralDegreeForm(forms.ModelForm):
    class Meta:
        model = models.GeneralDegreeInfo
        fields = (
                "school", 
                "graduated", 
                "faculty", 
                "department",
                "degree",
                "completion_status",
                "year_of_entered",
                "year_of_graduation"
                )

class MbaForm(forms.ModelForm):
    class Meta:
        model = models.MbaInfo
        fields = (
                "school", 
                "graduated", 
                "faculty", 
                "department",
                "degree",
                "completion_status",
                "year_of_entered",
                "year_of_graduation"
                )

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


