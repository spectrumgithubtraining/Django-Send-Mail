#### views.py
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from emailapp.forms import SendForm


def sendmail(request):
    form = SendForm()
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            subject = '*************Django Mail Sending************'
            message = 'Sending Email through Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('sendmail')
    return render(request, 'emailapp/home.html', {'form': form})