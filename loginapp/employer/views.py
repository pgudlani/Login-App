import os

from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from django.conf import settings
from employer.models import *
from employer.forms import *


class SignUpView(View):
  def get(self, request, *args, **kwargs):
    form = SignUpForm()
    return render_to_response('login.html', {'form' : form, 'login':False}, context_instance=RequestContext(request))

class LoginView(View):
  def get(self, request, *args, **kwargs):
   form = LoginForm(data=self.request.POST)
   error = '' 
   if form.is_valid():
	user = authenticate(username=request.POST['username'], password=request.POST['password'])

	if user is not None:
	  if user.is_active:
	   login(request, user)
	   return HttpResponseRedirect('/home/')
        elif User.objects.filter(username=request.POST['username']).exists():
          error = 'Wrong Password'
        else:
          error = 'Username does not exit'
   return render_to_response('login.html', {'form' : form, 'login' : True}, context_instance=RequestContext(request))


