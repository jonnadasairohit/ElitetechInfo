from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.shortcuts import render, reverse, redirect


# Create your views here.


def home(request):
    return render(request, "index.html")


def contactus(request):
    if request.method == 'POST':
        # Form validation
        print('I am sending email')
        print(request.POST)

        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            subject = request.POST.get("subject")
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_HOST_USER, ] # Venu address
            message = f"""
            Name: {request.POST.get('name', 'User')}\n
            Email: {request.POST.get('email', '')}\n
            Message: {request.POST.get('message')}
            """
            EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()

    return redirect(reverse("home"))
