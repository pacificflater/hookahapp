from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('index/', include('hookahapp.sklad.urls')),
    path('admin/', admin.site.urls)
]