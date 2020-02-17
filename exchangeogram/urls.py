
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('pages.urls')),
    path('user/', include('users.urls')),
    path('profile/', include('userprofile.urls')),
    path('site/admin/', admin.site.urls),
    path('feed/', include('post.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
