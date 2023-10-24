from django.contrib import admin
from django.urls import path, include
import django.contrib.auth.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('accounts.urls')),
    # for login
    path('accounts/', include("django.contrib.auth.urls")), 
]
