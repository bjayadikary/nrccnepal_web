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
    

# Testing
class TestProgram(models.Model):
    title = models.CharField(help_text="Program Title in less than 500 characters", max_length=500)
    time_duration = models.CharField(help_text="Program Duration, For instance, 'Every Saturday, 1 hour, ...", max_length=100)
    readtime = models.CharField(help_text="Expected Read Time of this Blog, like '5 mins'", max_length=50)
    short_description = models.CharField(help_text="Short Description in about one or two line", max_length=1000)
    program_featured_img = models.ImageField(upload_to="images/test_uploads/", blank=True, null=True)
    # program_featured_img_caption = models.CharField("Write caption for the image in less than 500 characters", max_length=500)
    program_tags = models.CharField(help_text="Mention some tags separated by comma (,)", max_length=500)

    slug = models.SlugField(unique=True, max_length=600)
    published_date = models.DateField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)
    PRIORITY_CHOICES = [
        (0, 'Do not display on homepage'),
        (1, 'Display in third column'),
        (2, 'Display in second column'),
        (3, 'Display in first column')
    ]
    priority_in_major_programs_list = models.IntegerField(help_text="Choose 0 if you don't want this program to display in homepage, else choose 1, 2, or 3 priority", choices=PRIORITY_CHOICES, default=0)
    priority_in_programs_list = models.IntegerField(help_text='0 means lowest priority', default=0)
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f"{self.title}"
    

class TestProgramTopic(models.Model):
    program_title = models.ForeignKey(TestProgram, on_delete=models.CASCADE)
    
    topic = models.CharField(help_text="Write a topic", max_length=500) # change it to topic name
    topic_order = models.IntegerField(help_text="1 to display this topic content on the first place, and similarly, 2 for second, 3 for third, and soon.", default=0, blank=True)
    
    topic_detail_first_paragraph = models.TextField(help_text="First paragraph", null=True, blank=True)
    topic_detail_first_bullet_points = models.TextField(help_text="Write bullet points in a single line separated by # ", null=True, blank=True)
    topic_detail_first_highlighting_text = models.TextField(null=True, blank=True)
    topic_detail_first_img = models.ImageField(upload_to=f"images/test_uploads/", blank=True, null=True)
    topic_detail_first_img_caption = models.CharField(help_text="Write caption for the image in less than 500 characters", max_length=500, blank=True, null=True)
    topic_detail_first_video_embed_source = models.CharField(help_text="Write the source of the video you want to embed. See the 'src' under iframe tag. Looks like: https://www.youtube.com/embed/sl18__huoXI?si=k0ZoEVYVihc-E9Pn ", max_length=200, blank=True, null=True)

    topic_detail_second_paragraph = models.TextField(help_text="Second Paragraph if exists", null=True, blank=True)
    topic_detail_second_bullet_points = models.TextField(help_text="Write bullet points in a single line separated by # ", null=True, blank=True)
    topic_detail_second_highlighting_text = models.TextField(null=True, blank=True)
    topic_detail_second_img = models.ImageField(upload_to=f"images/test_uploads", null=True, blank=True)
    topic_detail_second_img_caption = models.CharField(help_text="Write caption for the image in less than 500 characters", max_length=500, blank=True, null=True)
    topic_detail_second_video_embed_source = models.CharField(help_text="Write the source of the video you want to embed. See the 'src' under iframe tag. Looks like: https://www.youtube.com/embed/sl18__huoXI?si=k0ZoEVYVihc-E9Pn ", max_length=200, blank=True, null=True)

    topic_detail_third_paragraph = models.TextField(help_text="Third paragraph if exists", null=True, blank=True)
    topic_detail_third_bullet_points = models.TextField(help_text="Write bullet points in a single line separated by # ", null=True, blank=True)
    topic_detail_third_highlighting_text = models.TextField(null=True, blank=True)
    topic_detail_third_img = models.ImageField(upload_to=f"images/test_uploads", null=True, blank=True)
    topic_detail_third_img_caption = models.CharField(help_text="Write caption for the image in less than 500 characters", max_length=500, blank=True, null=True)
    topic_detail_third_video_embed_source = models.CharField(help_text="Write the source of the video you want to embed. See the 'src' under iframe tag. Looks like: https://www.youtube.com/embed/sl18__huoXI?si=k0ZoEVYVihc-E9Pn ", max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.topic}"