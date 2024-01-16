from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
# Create your views here.

def testhome(request):
    return render(request, 'core/index.html')

def home(request):
    return render(request, 'core/research.html')

def about(request):
    return render(request, 'core/about.html')

# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('fullname')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         content = request.POST.get('desc')

#         if name != "" and email != "" and phone != "" and content != "":
#             mycontact = Contact(name=name, email=email, phone=phone,
#                                 address=address, content=content)
#             mycontact.save()
#             # messages.success(request, 'Thank You For submitting form. We will reach you ASAP!!')

#         # else:
#             # messages.error(request, 'Please Fill Up the Form Correctly!!')

#     return render(request, 'core/contact.html')

def contact(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()
            messages.success(request, 'Thank you for submitting the form. We will reach out to you soon!')

        else:
            messages.error(request, 'Error sending the message!')
    else:
        contact_form = ContactForm()

    context = {'contact_form': contact_form}
    return render(request, 'core/contact.html', context)



def research(request):
    return render(request, 'core/research.html')


def spaceapps(request):
    return render(request, 'core/spaceapps.html')