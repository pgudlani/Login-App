from django import forms
from fileIn.models import *


class SignUpForm(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput, label="Your Name")
  email = forms.EmailField(widget=forms.TextInput, label="Email")
  username = forms.CharField(widget=forms.TextInput, label="Pick a Username")
  password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
  password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")

  class Meta:
    model = User
    fields = ['name','email','username']

  def clean(self):
    data = super(RegistrationForm, self).clean()
    if 'password1' in self.data and 'password2' in self.data:
      if self.data['password1'] != self.data['password2']:
        raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.data

  def save(self, commit=True):
    user = super(RegistrationForm, self).save(commit=False)
    user.set_password(self.data['password1'])
    if commit:
      user.save()
      return user



class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput, label='Username')
  password = forms.CharField(widget=forms.PasswordInput, label="Password")

  class Meta:
    fields = ['username','password']
