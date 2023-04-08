from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from registration.forms import CreateUserForm, CreateAirlineForm
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form_user = CreateUserForm(request.POST)
        form_airline = CreateAirlineForm(request.POST)
        if form_user.is_valid() and form_airline.is_valid():
            user = form_user.save(commit=False)
            user.is_active = False
            user.save()
            verify_email(request, user, form_user.cleaned_data.get('email'))
            airline = form_airline.save(commit=False)
            airline.user = user
            airline.budget = 3000000
            airline.save()
            return redirect("/accountcreated")
    else:
        form_user = CreateUserForm()
        form_airline = CreateAirlineForm()
    return render(request, "registration/signup.html", {"formuser" : form_user, "formairline" : form_airline})

def verify_email(request, user, email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('registration/activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[email])
    email.send()

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Email has been verified, you can login to your account.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('homepage')