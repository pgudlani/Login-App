from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from fileIn.models import *
from fileIn.forms import *

class LoginView(View):
  def post(self, request, *args, **kwargs):
    form = LoginForm(data=self.request.POST)
    error = ''
    if form.is_valid():
      user = authenticate(email=request.POST['username'], password=request.POST['password'])
#if user is None:
#  user = authenticate(email=request.POST['email'], password=request.POST['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/home/')
      else:
        error = 'User Not Present'
    else:
      error = 'Form Filling Not Correct'
    form = LoginForm()
    return render_to_response('login.html', {'form':form, 'error':error}, context_instance=RequestContext(request))

  def get(self, request, *args, **kwargs):
    form = LoginForm()
    return render_to_response('login.html', {'form' : form}, context_instance=RequestContext(request))
