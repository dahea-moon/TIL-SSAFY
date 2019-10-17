from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings # MASTER_APP/settings.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sns.urls')),
    # path('media', '/media/')
    path('accounts/', include('accounts.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
