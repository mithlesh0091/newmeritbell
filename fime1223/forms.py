

from .models import *
from django import forms

class reg_sign(forms.ModelsForm):
    School_Name = forms.CharFeild(widget=forms.TextInput(),required=True,max_length=100)
    Cant_find_your_School = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
    Contact_person_Name = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
    Designation_at_School = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
    Password1 = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
    Password2 = forms.CharFeild(widget=forms.EmailFeild(), required=True, max_length=100)
    Email = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)
    Mobile_No = forms.CharFeild(widget=forms.TextInput(), required=True, max_length=100)

    class Meta():
        model = reg_sign
        fields = ['School_Name','Cant_find_your_School','Contact_person_Name','Designation_at_Schoo','Password','Password2','Email','Mobile_No']






######################################################
################


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

############################
# forms.py
from django import forms



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
        class Meta:
            model = User
            fields = ('email', 'first_name', 'last_name', 'username')




class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
    ###########################
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)





# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


# from django.contrib.auth import get_user_model
# User = get_user_model()


# # Sign Up Form
# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
#     email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2',
#             ]


# # Profile Form
# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             ]
