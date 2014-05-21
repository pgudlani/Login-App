from django import forms
from employer.models import *

class SignUpForm(forms.ModelForm):
  
  class Meta:
    model = Company
    fields = ['name','website','year_founded','short_desc', 'long_desc', 'address', 'country', 'state', 'city', 'pincode', 'phone_number', 'corporate_type']

  def clean(self):
    data = super(SignUpForm, self).clean()
    if 'username' in self.data and User.objects.filter(username=self.data['username']).exists():
      raise forms.ValidationError("User there.")
            
    elif 'password1' in self.data and 'password2' in self.data:
      if self.data['password1'] != self.data['password2']:
        raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
      return self.data

    else:
      raise forms.ValidationError("Passwords not there.")

  def save(self, commit=True):
    user = super(SignUpForm, self).save(commit=False)
    user.set_password(self.data['password1'])
    if commit:
      user.save()
      return user
