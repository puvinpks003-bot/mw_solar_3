import os
import sys
import django
from django.conf import settings

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from solar.forms import CustomPasswordResetForm
from django.http import HttpRequest

request = HttpRequest()
request.META['SERVER_NAME'] = '127.0.0.1'
request.META['SERVER_PORT'] = '8000'

form = CustomPasswordResetForm(data={'email': 'puvinpks003@gmail.com'})
if form.is_valid():
    print("Form is valid!")
    try:
        form.save(
            request=request,
            use_https=False,
            from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', None),
            email_template_name='registration/password_reset_email.html',
            html_email_template_name='registration/password_reset_email_html.html',
            subject_template_name='registration/password_reset_subject.txt',
        )
        print("Save successful! Email sent.")
    except Exception as e:
        print(f"Exception during save: {e}")
else:
    print(f"Form errors: {form.errors}")
