from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from .forms import ContactForm
from .models import Project
from django.core.mail import EmailMessage

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


def about(request):
    projects = Project.objects.all()    # for navbar link 'Projects' dropdown-menu
    return render(request, 'about.html', {'projects': projects})


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    projects = Project.objects.all()    # for navbar link 'Projects' dropdown-menu
    context = {'project': project, 'projects': projects}
    return render(request, 'project_details.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # get the form data
            name = form.cleaned_data['name']    # possibly change to cleaned_data.get() and creating validationerror?
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # construct email message
            subject= f'Porfolio message from {name}'
            from_email = 'admin@example.com'
            to_email = ['admin@example.com']
            # from_email = settings.CONTACT_EMAIL
            # to_email = settings.ADMIN_EMAIL
            email_message = EmailMessage(subject, message, from_email, to_email)

            # send the email
            email_message.send()
            
            # message() add confirmation message on web page
            projects = Project.objects.all()
            return render(request, 'home.html', {'projects': projects})
    else:
        projects = Project.objects.all()
        form = ContactForm()
        return render(request, 'contact.html', {'form': form, 'projects': projects})
    

def resume(request):
    projects = Project.objects.all()    # for navbar link 'Projects' dropdown-menu
    return render(request, 'resume.html', {'projects': projects})
