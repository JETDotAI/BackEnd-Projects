# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import (
	authenticate,
	login,
	logout,
	)

def login_view(request):
	if 'registration' in request.POST:
		new_user ,created= User.objects.get_or_create(username = request.POST.get("new_email",False), email = request.POST.get("new_email", False))
		if created:
			new_user.set_password(request.POST.get("new_password", False))
			new_user.save()

	if 'login' in request.POST:
		post_username = request.POST.get("username", False)
		post_password = request.POST.get("password", False)

		user = authenticate(username = post_username, password = post_password)
		if user is not None:
			if user.is_active:
				login(request, user)

	if request.user.is_authenticated:
		return HttpResponseRedirect('/posts/')
	else:
		return render(request, "login_form.html", {})
	
def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

