from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from employer.constants import country_choices,corporate_choices


class Company(models.Model):
  """
    By default Company has a EUser assosiated to it as owner which has all the privileges.
  """
  name = models.CharField(unique=True, max_length=100)
  website = models.URLField(unique=True, max_length=300)
  year_founded = models.SmallIntegerField(null=True)
  short_desc = models.CharField(max_length=200)
  long_desc = models.TextField(null=True)
  address = models.CharField(max_length=300)
  country = models.CharField(max_length=10, choices=country_choices, default='India')
  state = models.CharField(max_length=40)
  city = models.CharField(max_length=40)
  pincode = models.IntegerField()
  phone_number = models.CharField(max_length=15)   #CharField as '+91' or any country code would also be given
  corporate_type = models.CharField(max_length=10, choices=corporate_choices)
  owner = models.ForeignKey('EUser', related_name='companies_owned')

  def __unicode__(self):
    return self.name


class EUser(AbstractBaseUser):
  """
    EUser - Employee User
  """
  username = models.CharField(max_length=50, unique=True, db_index=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  mobile_number = models.CharField(max_length=15, unique=True)
  email = models.EmailField(unique=True)
  alt_email = models.EmailField(unique=True)       # Alternate Email
  company = models.ForeignKey(Company, related_name='eusers', null=True)    # null=True as first a user is created then is assigned to a company
  role = models.ForeignKey('Role', null=True)     # null=True as role is assigned after the user is created
  
  USERNAME_FIELD = 'username'
  
  def __unicode__(self):
    return self.username + ' :: ' + self.first_name + ' ' + self.last_name


class Privilege(models.Model):
  """
    Privileges need to be added into the database to be used as a ManyToManyField
  """
  name = models.CharField(max_length=100)

  def __unicode__(self):
    return self.name

class Role(models.Model):
  """
    Role specific to a company contains priveleges which could be assigned to many users
    Example - 'Intern' is a role and can be assigned to many EUsers
  """
  name = models.CharField(max_length=30)
  company = models.ForeignKey(Company)
  desc = models.TextField(null=True)
  privileges = models.ManyToManyField(Privilege)

  def __unicode__(self):
    return self.company.name + ' :: ' + self.name
