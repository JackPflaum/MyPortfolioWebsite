from django import forms
from django.core import validators
from validate_email_address import validate_email

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(max_length=255,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}),
                             validators=[validators.EmailValidator(message='Invalid email')])
    message = forms.CharField(max_length=2000,
                              widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not validate_email(email):
    #         raise forms.ValidationError('Invalid email address. Please enter a valid email')
    #     return email



# good example and how to set up email:
# https://mailtrap.io/blog/django-contact-form/

# another good example:
# https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid
