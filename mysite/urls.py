
##django
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
# polls
from profile import views 
from employee import views as emp
from RequestsLicense import views as license

urlpatterns = [
    # vistas generales
    path('admin/', admin.site.urls),
    path ('users/login/', views.login_view, name='login'),
    path('signup/',views.signup_view, name='signup'),
    path('logout/', views.logout_view, name = 'logout'),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change-password.html',
            success_url = reverse_lazy('change_password')
        ),
        name='change_password'
    ),
    # vistas sin acceso de admin
    path('dashboard/', emp.dashboard_view, name='dashboard'),
    path('solicitud/', license.request_license, name='request_license'),
    path('profile/',emp.update_profile,name="update_profile"),

    # vistas admin
] 