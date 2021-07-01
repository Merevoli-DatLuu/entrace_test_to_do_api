from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('user_auth.urls')),
    path('api/v1/todo/', include('todo.urls')),
    path('api/v1/user/', include('user.urls')),
]
