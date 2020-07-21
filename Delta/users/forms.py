from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile



# class SignupForm(forms.Form):
#     first_name = forms.CharField(max_length=30, label='First name')
#     last_name = forms.CharField(max_length=30, label='Last name')
#
#     def signup(self, request, users):
#         users.first_name = self.cleaned_data['first_name']
#         users.last_name = self.cleaned_data['last_name']
#
#         up = users.profile
#         up.phone_number = self.cleaned_data['phone_number']
#         up.job_title = self.cleaned_data['job_title']
#         users.save()
#         up.save()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','username')

class  ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')