from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=250, blank=False)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, default="")
    content = models.TextField()

    def __str__(self) -> str:
        return self.name
