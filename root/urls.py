from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
