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
