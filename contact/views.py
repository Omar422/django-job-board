from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send_message(request):
    info = Info.objects.first()

    if request.method == 'POST':
        subject = 'New Contact From JobBoard.com'
        message = f'You Have an Email From: "{request.POST["email"]}"'
        message += f'\n\nHis Email Subject Is: "{request.POST["subject"]}"'
        message += f"\n\nMessage:\n\n\"{request.POST['message']}\""
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER]
    )

    return render(request, 'contact/contact.html', {
        'myInfo':info
        })