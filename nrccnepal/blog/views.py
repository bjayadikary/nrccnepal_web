from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from django.template.defaultfilters import slugify
from .models import Blogs, TrendingBlogs


# Create your views here.

def blog(request):
	# Retriving the top blogs with highest priority
	trending_blogs = TrendingBlogs.objects.all().order_by('priority')

	all_blogs = Blogs.objects.all().order_by('priority','-updated_datetime','-published_date')
	paginator = Paginator(all_blogs, 4) # number of objects to display per page
	current_page = request.GET.get('page') # retreives current page number

	try:
		paginator_objects = paginator.page(current_page)
	except PageNotAnInteger:
		paginator_objects = paginator.page(1)

	return render(request, "blog/blog-page.html", {
		"blogs" : paginator_objects,
		"trending_blogs": trending_blogs,
		})


def single_blog(request, slug):
	# Retriving the top blogs with highest priority
	trending_blogs = TrendingBlogs.objects.all().order_by('priority')

	blog = Blogs.objects.filter(slug=slug).first()
	return render(request, "blog/single-blog.html", {
		"blog": blog,
		"trending_blogs": trending_blogs,
		})
