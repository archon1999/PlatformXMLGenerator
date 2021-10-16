from django.urls import path

from apps.frontend import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(),
         name='registration'),
    path('registration/confirm', views.RegistrationConfirmView.as_view(),
         name='registration_confirm'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('settings/', views.UserSettingsView.as_view(), name='settings'),
]
