from django.db import models
from django.contrib.auth.models import AbstractBaseUser


def get_file_upload(instance, filename):
  return '/'.join([instance.user.username, filename]) 

class User(AbstractBaseUser):
  """
    The user model for login and authenticating
    abstract User - Custom User Class
  """
  username = models.CharField(max_length=100, unique=True, db_index=True)
  name = models.CharField(max_length=100)
  email = models.EmailField()
  date_joined = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'username'

  def __unicode__(self):
    return self.username + ' :: ' + self.name


class File(models.Model):
  """
    The File model for storing the file
  """
  user = models.ForeignKey(User)
  name = models.CharField(max_length=100)
  description = models.TextField()
  filename = models.FileField(upload_to=get_file_upload, max_length=1000)
  date_added = models.DateTimeField(auto_now_add=True)
  
  def __unicode__(self):
    return self.name
