from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# Create your models here.
def validate_if_between_1_3(value):
    if value <= 3 and value >=1:
        return value
    else:
        raise ValidationError("Values should be 1, 2, or 3 representing corresponding column in NRCC's program in home page, else specify 0 for default")

class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=250, blank=False)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, default="")
    content = models.TextField()

    def __str__(self) -> str:
        return self.name
       

class Programs(models.Model):
    title = models.CharField("Program Title", max_length=500)
    body_intro = models.TextField(default="Type here...") # should change to introduction that describes the event in may be less than 50 words and that comes just below the featured_image.  
    published_date = models.DateField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)
    # program_in_home_flag = models.BooleanField(default=False)
    priority_in_home = models.IntegerField(default=0, blank=True, validators=[validate_if_between_1_3]) # validation should be between 0 and 4, 0 for default case with which the particular blog won't be displayed in the home page
    priority_in_programs = models.IntegerField(default=0) # rename to priority_in_programs_list
    featured_image = models.ImageField(upload_to="images/test_uploads/", blank=True, null=True, default='default/no_image.jpg')
    slug = models.SlugField(unique=True, max_length=600)

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f"{self.title}"