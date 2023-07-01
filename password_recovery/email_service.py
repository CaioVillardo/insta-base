from django.core.mail import send_mail
from django.conf import settings

def send_password_reset_email(user_email, reset_link):
    subject = 'Recuperação de Senha'
    message = f'Olá,\n\nVocê solicitou a recuperação de senha para a sua conta.\n\nClique no link abaixo para redefinir sua senha:\n\n{reset_link}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
