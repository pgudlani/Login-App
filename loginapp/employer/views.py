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
  def post(self, request, *args, **kwargs):
    form = SignUpForm(data=self.request.POST)
    error = ''
    if form.is_valid():
      user = form.save()
      return HttpResponseRedirect('../home/')
    return render_to_response('login.html', {'form':form, 'error':error, 'login':False}, context_instance=RequestContext(request))
  def get(self, request, *args, **kwargs):
    form = SignUpForm()
    return render_to_response('login.html', {'form' : form, 'login':False}, context_instance=RequestContext(request))

class LoginView(View):
  def post(self, request, *args, **kwargs):
   form = LoginForm(data=self.request.POST)
   error = '' 
   if form.is_valid():
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
	  if user.is_active:
	   login(request, user)
	   return HttpResponseRedirect('../home/')
        elif EUser.objects.filter(username=request.POST['username']).exists():
          error = 'Wrong Password'	
        else:
          error = 'Username does not exit'
   return render_to_response('login.html', {'form' : form, 'login' : True, 'error' : error}, context_instance=RequestContext(request))

  def get(self, request, *args, **kwargs):
  # if self.request.user and self.request.user.is_active:
   #  return HttpResponseRedirect('/home/')
   form = LoginForm()
   return render_to_response('login.html', {'form' : form, 'login' : True}, context_instance=RequestContext(request))


