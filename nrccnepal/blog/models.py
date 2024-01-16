from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# Create your models here.
def validate_if_between_1_10(value):
	if value <=10 and value >=0:
		return value
	else:
		raise ValidationError("This field only accepts integers between 0 and 10")

def validate_if_between_1_4(value):
	if value <=4 and value >=1:
		return value
	else:
		raise ValidationError("Values should be between 1 and 4 representing rows of Trending block")


class Authors(models.Model):
	author = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	author_icon = models.ImageField(upload_to="images/test_uploads/", blank=True, null=True, default='default/no_image.jpg')
	mail = models.EmailField(max_length=200)
	joined_date = models.DateField()
	priority = models.IntegerField(default=0, validators=[validate_if_between_1_10])


	def __str__(self):
		return f"{self.author}"


class Blogs(models.Model):
	author = models.ForeignKey(Authors, on_delete=models.PROTECT)
	title = models.CharField("Blog Title", max_length=500)
	body = models.TextField(default="Type here...")
	published_date = models.DateField(auto_now_add=True, blank=True)
	updated_datetime = models.DateTimeField(auto_now=True, blank=True)
	priority = models.IntegerField(default=0, validators=[validate_if_between_1_10])
	# thumbnail = models.ImageField(upload_to="images/test_uploads/", blank=True, null=True, default='default/no_image.jpg')
	featured_image = models.ImageField(upload_to="images/test_uploads/", blank=True, null=True, default='default/no_image.jpg')
	# trending_priority = models.IntegerField(default=0, blank=True, validators=[validate_if_between_1_4])
	slug = models.SlugField(unique=True, max_length=600)

	def save(self):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save()

	def __str__(self):
		return f"{self.title}"


class TrendingBlogs(models.Model):
	blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	priority = models.IntegerField(blank=False, null=False, unique=True, validators=[validate_if_between_1_4])

	def __str__(self):
		return f"{self.blogs.title}"


class UserComments(models.Model):
	blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=200)
	message = models.TextField(default="Here goes your Comments...")
	date = models.DateField(auto_now_add=True, blank=True)

	def __str__(self):
		return f"Comments of {self.name}"
