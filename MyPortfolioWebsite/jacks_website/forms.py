from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(max_length=255,
                             widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}), max_length=2000)



# good example and how to set up email:
# https://mailtrap.io/blog/django-contact-form/

# another good example:
# https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid
