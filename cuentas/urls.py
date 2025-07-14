from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.profile_view, name='profile'),
    path('perfil/editar/', views.edit_profile, name='edit_profile'),
]


from django.contrib.auth import views as auth_views

urlpatterns = [
    path('perfil/', views.profile_view, name='profile'),
    path('perfil/editar/', views.edit_profile, name='edit_profile'),
    path('perfil/password/', auth_views.PasswordChangeView.as_view(
        template_name='cuentas/change_password.html',
        success_url='/cuentas/perfil/'
    ), name='change_password'),
]


