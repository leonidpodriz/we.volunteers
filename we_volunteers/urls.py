from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('landing.urls'), name='landing'),
    path('admin/', admin.site.urls),
]
