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
      user = authenticate(username=request.POST['username'], password=request.POST['password'])
#if user is None:
#  user = authenticate(email=request.POST['email'], password=request.POST['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/home/')
      elif User.objects.filter(username=request.POST['username']).exists():
        error = 'Wrong Password'
      else:
        error = 'User Not There'
    return render_to_response('login.html', {'form':form, 'error':error}, context_instance=RequestContext(request))

  def get(self, request, *args, **kwargs):
    if self.request.user and self.request.user.is_active:
      return HttpResponseRedirect('/home/')
    form = LoginForm()
    return render_to_response('login.html', {'form' : form}, context_instance=RequestContext(request))


class SignUpView(View):
  def post(self, request, *args, **kwargs):
    form = SignUpForm(data=self.request.POST)
    error = ''
    if form.is_valid():
      user = form.save()
      return HttpResponseRedirect('/home/')
    return render_to_response('login.html', {'form':form, 'error':error}, context_instance=RequestContext(request))
  def get(self, request, *args, **kwargs):
    if self.request.user and self.request.user.is_active:
      return HttpResponseRedirect('/home/')
    form = SignUpForm()
    return render_to_response('login.html', {'form' : form}, context_instance=RequestContext(request))


class HomeView(ListView):
  model = File
  template_name = 'file_list.html'
  context_object_name = 'files'
  
  def dispatch(self, *args, **kwargs):
    if self.request.user and self.request.user.is_active:
      return super(HomeView, self).dispatch(*args, **kwargs)
    else:
      return HttpResponseRedirect('/login/')
  
  

class LogoutView(View):
  def get(self, request, *args, **kwargs):
    logout(self.request)
    return HttpResponseRedirect('/login/')


class UploadView(View):
  def post(self, request, *args, **kwargs):
    self.request.POST['user'] = self.request.user.id
    form = FileUploadForm(self.request.POST, self.request.FILES)
    print form
    if form.is_valid():
      user = form.save()
    return HttpResponseRedirect('/home/')
