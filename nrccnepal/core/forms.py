from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'address', 'phone', 'content']
		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': "Your Name",'data-sb-validations':"required", 'data-rule':"minlen:4", 'data-msg':'Please enter at least 4 chars'}),
		'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': "Your Email",'data-sb-validations':"required", 'data-rule':"email", 'data-msg':"Please enter a valid email"}),
		'address': forms.TextInput(attrs={'class': 'form-control', 'id': 'address', 'placeholder': "Your Address", 'data-sb-validations':"required", }),
		'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': "Your Phone Number", 'data-sb-validations':"required"}),
		'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': "Message", 'cols': 30, 'rows': 10, 'data-sb-validations':"response"})
		}
