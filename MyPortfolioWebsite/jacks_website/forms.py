from django import forms
from django.core import validators
from validate_email_address import validate_email

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(max_length=255,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    message = forms.CharField(max_length=2000,
                              widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))


# good example and how to set up email:
# https://mailtrap.io/blog/django-contact-form/

# another good example:
# https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid
