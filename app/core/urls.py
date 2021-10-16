from django.contrib import admin
from django.urls import path, re_path, include


urlpatterns = [
    re_path(r'^jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', include('apps.frontend.urls'))
]
