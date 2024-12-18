from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from FileUploader import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('upload/', views.upload_file, name='upload'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
