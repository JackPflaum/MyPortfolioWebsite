from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from .forms import ContactForm
from .models import Project
from django.core.mail import EmailMessage
from django.contrib import messages
import os
from dotenv import load_dotenv, find_dotenv

# load environmental variables from .env file
load_dotenv(find_dotenv())


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {'project': project}
    return render(request, 'project_details_mobile.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # get the form data
            name = form.cleaned_data['name']    # possibly change to cleaned_data.get() and creating validationerror?
            email = form.cleaned_data['email']
            form_message = form.cleaned_data['message']

            # construct email message
            subject= f'Porfolio website message from {name}'
            message = email + '\n\n' + form_message    # add senders email address to top of message
            from_email = 'jackpflaum@gmail.com'
            to_email = [os.environ.get('TO_EMAIL')]
            email_message = EmailMessage(subject, message, from_email, to_email)

            # send the email
            email_message.send()
            
            # confirmation message on web page
            messages.success(request, 'Thank you for the message. I will get back to you shortly.')

            return render(request, 'home.html', {})
        else:
            messages.warning(request, 'Invalid email. Please try again.')
            return redirect('home')
    else:
        return render(request, 'contact.html', {'form': form})
    

def resume(request):
    return render(request, 'resume.html', {})
