# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
# Create your views here.

	
#POSTS LISTS
def post_list(request):
	html =''
	list_posts = Post.objects.all()
	query = request.GET.get("query")
	if query:
		list_posts = list_posts.filter(
		
		Q(title__icontains = query)|
		Q(content__icontains = query)|
		Q(author__contains = query)|
		Q(publish__icontains = query)
		).distinct()
		
	paginator = Paginator(list_posts, 10) 
	page_request_var = "page"
	page = request.GET.get(page_request_var)
		
	try:
		get_post = paginator.page(page)
	except PageNotAnInteger:
		get_post = paginator.page(1)
	except EmptyPage:
		get_post = paginator.page(paginator.num_pages)
	
	context = {
	"list_posts": get_post,
	"title": "Django Blogs Gaming",
	"page_request_var": page_request_var,

	}
	return render(request, "post_list.html", context)
	
		
#POSTS DETAILS
def post_detail(request, id = None):
	obj_instance = get_object_or_404(Post, id = id)
	context = {
		"title": obj_instance.title,
		"object_instance": obj_instance,
	}
	return render(request, "post_detail.html", context)
	
#POSTS CREATE 
def post_create(request):
	
	if not request.user.is_authenticated():
		raise Http404
		
	createform = PostForm(request.POST or None, request.FILES or None)
	context = {
		"create_form": createform,
	}
	
	if createform.is_valid():
		obj_instance = createform.save(commit = False)
		obj_instance.author = request.user
		obj_instance.save()
		messages.success(request, "POST SUCCESSFULLY CREATED")
		return HttpResponseRedirect('/posts')
		
	return render(request, "post_form.html", context)

#POSTS UPDATE
def post_update(request, id = None):
	if not request.user.is_authenticated():
		raise Http404
		
	obj_instance = get_object_or_404(Post, id = id)
	createform = PostForm(request.POST or None,request.FILES or None, instance = obj_instance)

	if createform.is_valid():
		obj_instance = createform.save(commit = False)
		obj_instance.save()
		messages.success(request, "POST SUCCESSFULLY UPDATED")
		return HttpResponseRedirect(obj_instance.get_absolute_url())
	
	context = {
		"title": obj_instance.title,
		"object_instance": obj_instance,
		"create_form": createform,
	}
	return render(request, "post_form.html", context)

#POSTS DELETE
def post_delete(request, id = None):
	if not request.user.is_authenticated():
		raise Http404
		
	obj_instance = get_object_or_404(Post, id = id)
	obj_instance.delete()
	messages.success(request, "POST SUCCESSFULLY DELETED")
	return redirect("posts:list")
	
#PAGINATION
def listing(request):
    contact_list = Contacts.objects.all()

    return render(request, 'list.html', {'contacts': contacts})



