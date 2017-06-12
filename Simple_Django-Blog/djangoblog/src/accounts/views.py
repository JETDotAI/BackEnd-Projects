# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

# Create your views here.
#LOGIN 
def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		login(request, user)
		return HttpResponseRedirect('/posts')
	context = {
		"form":form,
		"title":title
	}
	return render (request, "login_form.html", context)
	
def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit = False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		return HttpResponseRedirect('/login')
		
	context = {
		"form": form,
		"title": title,
		
	}
	return render (request, "login_form.html", context)
	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login')
