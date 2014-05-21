from django.conf import settings
from django.contrib.auth.models import check_password

from employer.models import EUser

class CustomAuthBackend(object):
  def authenticate(self, username=None, password=None):
    try:
      user = EUser.objects.get(username=username)
      if user.check_password(password):
	return user
    except EUser.DoesNotExist:
	return None

  def get_user(self,user_id):
    try:
      user = EUser.objects.get(pk=user_id)
      if user.is_active():
	return user
      return None
    except EUser.DoesNotExist:
      return None

