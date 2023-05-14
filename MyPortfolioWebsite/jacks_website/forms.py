from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=255)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)



# good example and how to set up email:
# https://mailtrap.io/blog/django-contact-form/

# another good example:
# https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid
