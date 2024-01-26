from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_email_with_attachment(to_email, subject, message, image_path):
    # Prepare email content
    text_content = strip_tags(message)
    email = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_email])

    # Optionally, you can embed the image in the email
    # You can use this if you want to display the image inline in the email body
    image_data = open(image_path, 'rb').read()
    email.attach_alternative(f'<img src="cid:image1">', 'text/html')
    email.attach('image1', image_data, 'image/jpeg')

    # Send the email
    email.send()

def send_email_attachment(to_email, subject, message, image_path):
    text_content = strip_tags(message)
    email = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [to_email])

    # Attach the image file
    with open(image_path, 'rb') as image_file:
        email.attach_file(image_file.name)
    
    email.send()