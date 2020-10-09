#
#
# from .models import *
# from django import forms
#
# class reg_sign(forms.ModelsForm):
#     School_Name = forms.CharFeild(widget=forms.TextInput(),required=True,max_length=100)
#     Cant_find_your_School = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Contact_person_Name = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Designation_at_School = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Password1 = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Password2 = forms.CharFeild(widget=forms.EmailFeild(), required=True, max_length=100)
#     Email = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#     Mobile_No = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
#
#     class Meta():
#         model = reg_sign
#         fields = ['School_Name','Cant_find_your_School','Contact_person_Name','Designation_at_Schoo','Password','Password2','Email','Mobile_No']
#
#
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Customer,Employee,Consultancy

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    location = forms.CharField(required=True)
    # image = forms.ImageField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.location = self.cleaned_data.get('location')
        # customer.image = self.cleaned_data.get('image')
        customer.save()
        return user
###################################################################

###################################################################

class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        employee = Employee.objects.create(user=user)
        employee.phone_number = self.cleaned_data.get('phone_number')
        employee.designation = self.cleaned_data.get('designation')
        employee.save()
        return user

class ConsultancyForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_consultancy = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        consultancy = Consultancy.objects.create(user=user)
        consultancy.phone_number = self.cleaned_data.get('phone_number')
        consultancy.designation = self.cleaned_data.get('designation')
        consultancy.save()
        return user


from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)