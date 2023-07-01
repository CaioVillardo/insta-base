from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .hashing_utils import hash_password
from .token_manager import TokenManager
from .authorization_service import has_permission
from .activity_logger import log_activity
from .email_service import send_password_reset_email

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            User.objects.get(username=username)
            messages.error(request, 'Nome de usuário já está em uso.')
        except ObjectDoesNotExist:
            hashed_password = hash_password(password)
            user = User.objects.create_user(username=username, password=hashed_password, email=email)
            messages.success(request, 'Registro realizado com sucesso.')

def user_password_reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            token = TokenManager.generate_token(user)
            messages.success(request, 'E-mail de redefinição de senha enviado com sucesso.')
        except ObjectDoesNotExist:
            messages.error(request, 'O e-mail fornecido não está registrado.')

def user_password_reset_confirm(request, token):
    if request.method == 'POST':
        password = request.POST['password']
        user = User.objects.get(id=request.user.id)
        if TokenManager.verify_token(user, token):
            messages.success(request, 'Senha redefinida com sucesso.')
        else:
            messages.error(request, 'Token inválido ou expirado.')

def view_resource(request, resource_id):
    resource_type = "resource"
    if has_permission(request.user, resource_id, resource_type):
        return HttpResponse("Recurso exibido")
    else:
        return HttpResponse("Você não tem permissão para acessar este recurso")

def create_post(request):
    if request.method == 'POST':
        log_activity(request.user, 'Criou uma nova postagem')

        return redirect('pagina_de_sucesso')
    else:
        return render(request, 'create_post.html')

def request_password_reset(request):
    if request.method == 'POST':
        send_password_reset_email(request.POST['email'], reset_link)

        return redirect('pagina_de_sucesso')
    else:
        return render(request, 'password_reset_request.html')

