from django import forms
from django.db.models import Q

from employer.models import *

class SignUpForm(forms.ModelForm):
  """
    SignUpForm for a company which includes a company signup with a user signup as an owner also.
    Extra Fields are for owner details.
  """
  username = forms.CharField(widget=forms.TextInput, label="Pick a Username")
  first_name = forms.CharField(widget=forms.TextInput, label="First Name")
  last_name = forms.CharField(widget=forms.TextInput, label="Last Name")
  mobile_number = forms.CharField(widget=forms.TextInput, label="Mobile Number")
  email = forms.EmailField(widget=forms.TextInput, label="Email")
  alt_email = forms.EmailField(widget=forms.TextInput, label="Alternate Email")
  password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
  password2 = forms.CharField(widget=forms.PasswordInput, label="Password (again)")
 
  class Meta:
    model = Company
    fields = ['name','website','year_founded','short_desc', 'long_desc', 'address', 'country', 'state', 'city', 'pincode', 'phone_number', 'corporate_type']

  def clean(self):
    """
      clean function -> For all the validation process before saving the data.
    """
    data = super(SignUpForm, self).clean()
    if 'username' in self.data and EUser.objects.filter(username=self.data['username']).exists():
      raise forms.ValidationError("User there.")
#  This validates if username is unique. Same for the rest

    elif 'mobile_number' in self.data and EUser.objects.filter(mobile_number=self.data['mobile_number']).exists():
      raise forms.ValidationError("Mobile Number should be unique.")

    elif 'email' in self.data and EUser.objects.filter(Q(email=self.data['email']) | Q(alt_email=self.data['email'])).exists():
      raise forms.ValidationError("Email should be unique.")

    elif 'alt_email' in self.data and EUser.objects.filter(Q(email=self.data['alt_email']) | Q(alt_email=self.data['alt_email'])).exists():
      raise forms.ValidationError("Alternate Email should be unique.")

    elif 'email' in self.data and 'alt_email' in self.data and self.data['email']==self.data['alt_email']:
      raise forms.ValidationError("Email and Alternate Email should be different.")
            
#  Checks if the passwords entered matches or not
    elif 'password1' in self.data and 'password2' in self.data:
      if self.data['password1'] != self.data['password2']:
        raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
      return self.data

    else:
      raise forms.ValidationError("Passwords not there.")

  def save(self, commit=True):
    company = super(SignUpForm, self).save(commit=False)       # commit=false implies it waits for the EUser instance to be created

    username = self.data['username']
    first_name = self.data['first_name']
    last_name = self.data['last_name']
    mobile_number = self.data['mobile_number']
    email = self.data['email']
    alt_email = self.data['alt_email']
    user = EUser.objects.create(
        username = username,
        first_name = first_name,
        last_name = last_name,
        mobile_number = mobile_number,
        email = email,
        alt_email = alt_email
    )
    user.set_password(self.data['password1'])
    company.owner = user

    if commit:
      company.save()
      user.company = company
      user.save()
      return company
      
class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput, label='Username')
  password = forms.CharField(widget=forms.PasswordInput, label='Password')

  class Meta:
    fields = ['username','password']



