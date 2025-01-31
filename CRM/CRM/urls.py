from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include("home.urls")),
    path('items/',include('items.urls')),
    path('',include('home.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('inbox/',include('conversation.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
