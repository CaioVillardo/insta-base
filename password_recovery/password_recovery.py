from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .email_service import send_password_reset_email

def request_password_reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            reset_link = request.build_absolute_uri(
                f'/password-reset/{user.pk}/{token}/'
            )

            send_password_reset_email(email, reset_link)

            messages.success(request, 'Um e-mail de recuperação de senha foi enviado.')
            return redirect('pagina_de_sucesso')
        except User.DoesNotExist:
            messages.error(request, 'O e-mail informado não está associado a uma conta.')
            return redirect('pagina_de_erro')
    else:
        return render(request, 'password_reset_request.html')
