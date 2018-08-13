from urllib.parse import quote_plus
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
# Create your views here.
from .models import Post

# CREATE ARTICLE
def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Successfully created.!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post/post_form.html", context)

# DETAIL VIEW FOR ALL ARTICLE
def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404

	context = {
		"title": instance.title,
		"instance": instance,
		}
	return render(request, "post_list/post_detail.html", context)

# ALL ARTICLES VIEW
def post_list(request):
	today = timezone.now().date()
	queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now()) #active()
	paginator = Paginator(queryset_list, 6)
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Post.objects.all()

	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
		
	context = {
		"object_list": queryset,
		"title": "Breaking News",
		"page_request_var": page_request_var,
		"today": today,
	}
	
	return render(request, "post_list/post_list.html", context)

# LIST FOR POLITICAL ARTICLES
def post_politics_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.filter(category='politics').all()
	queryset_politics_list = Post.objects.filter(category='POLITICS').filter(draft=False).filter(publish__lte=timezone.now())
	paginator = Paginator(queryset_politics_list, 6)
	if request.user.is_staff or request.user.is_superuser:
		queryset_politics_list = Post.objects.filter(category='POLITICS').all()

	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
		
	context = {
		"queryset_politics_list": queryset,
		"title": "Political News",
		"page_request_var": page_request_var,
		"today": today,
	}
	
	return render(request, "post_list/post_politics_list.html", context)

# THE LIST FOR EVENT POSTS
def post_events_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.filter(category='politics').all()
	queryset_politics_list = Post.objects.filter(category='EVENTS').filter(draft=False).filter(publish__lte=timezone.now())
	paginator = Paginator(queryset_politics_list, 6)
	if request.user.is_staff or request.user.is_superuser:
		queryset_politics_list = Post.objects.filter(category='EVENTS').all()

	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
		
	context = {
		"queryset_politics_list": queryset,
		"title": "Events News",
		"page_request_var": page_request_var,
		"today": today,
	}
	
	return render(request, "post_list/post_events_list.html", context)

# THE LIST FOR GIST POSTS
def post_gist_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.filter(category='politics').all()
	queryset_politics_list = Post.objects.filter(category='GIST').filter(draft=False).filter(publish__lte=timezone.now())
	paginator = Paginator(queryset_politics_list, 6)
	if request.user.is_staff or request.user.is_superuser:
		queryset_politics_list = Post.objects.filter(category='GIST').all()

	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
		
	context = {
		"queryset_politics_list": queryset,
		"title": "Gists News",
		"page_request_var": page_request_var,
		"today": today,
	}
	
	return render(request, "post_list/post_gist_list.html", context)

# THE LIST FOR CELEBRITIES POSTS
def post_celeby_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.filter(category='politics').all()
	queryset_politics_list = Post.objects.filter(category='CELEBS').filter(draft=False).filter(publish__lte=timezone.now())
	paginator = Paginator(queryset_politics_list, 6)
	if request.user.is_staff or request.user.is_superuser:
		queryset_politics_list = Post.objects.filter(category='CELEBS').all()

	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)
		
	context = {
		"queryset_politics_list": queryset,
		"title": "Celebrities News",
		"page_request_var": page_request_var,
		"today": today,
	}
	
	return render(request, "post_list/post_celeb_list.html", context)

# UPDATE ARTICLE
def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		messages.success(request, "Successfully updated.!")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
		}
	return render(request, "post/post_form.html", context)

## DELETE ARTICLE
def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully Deleted.!")
	return redirect("posts:list")
	
	