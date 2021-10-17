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

     path('platform/<int:platform_id>/', views.PlatformView.as_view(),
          name='platform'),
     path('platform/<int:platform_id>/projects/new/',
          views.NewProjectView.as_view(), name='new_project'),
     path('platform/<int:platform_id>/project/<int:project_id>/edit/',
          views.EditProjectView.as_view(), name='edit_project'),
     path('platform/<int:platform_id>/project/<int:project_id>/delete/',
          views.DeleteProjectView.as_view(), name='delete_project'),
     path('platform/<int:platform_id>/project/<int:project_id>/',
          views.ProjectView.as_view(), name='project'),
     path('platform/<int:platform_id>/projects/reorder/',
          views.ProjectsReOrderView.as_view(), name='projects_reorder'),
     path('platform/<int:platform_id>/project/<int:project_id>/categories/new/',
          views.ProjectNewCategoryView.as_view(), name='project_new_category'),
     path('platform/<int:platform_id>/project/<int:project_id>/categories/delete/',
          views.ProjectDeleteCategoryView.as_view(),
          name='project_delete_category'),
]
