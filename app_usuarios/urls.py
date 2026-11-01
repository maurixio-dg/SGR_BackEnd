
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [

    # ==========================================
    # GESTIÓN DE USUARIOS - CRUD
    # ==========================================

    path(
        '',
        views.listar_usuarios,
        name='listar_usuarios'
    ),

    path(
        'nuevo/',
        views.crear_usuario,
        name='crear_usuario'
    ),

    path(
        '<int:pk>/editar/',
        views.editar_usuario,
        name='editar_usuario'
    ),

    path(
        '<int:pk>/cambiar-estado/',
        views.cambiar_estado_usuario,
        name='cambiar_estado_usuario'
    ),


    # ==========================================
    # RECUPERACIÓN DE CONTRASEÑAS
    # ==========================================

    # 1. Solicitar recuperación por correo
    path(
        'recuperar/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            email_template_name='registration/password_reset_email.html',
            subject_template_name='registration/password_reset_subject.txt',
        ),
        name='password_reset'
    ),

    # 2. Confirmación de solicitud enviada
    path(
        'recuperar/enviado/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # 3. Validación de token y nueva contraseña
    path(
        'restablecer/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    # 4. Contraseña restablecida correctamente
    path(
        'restablecer/completado/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),

]
