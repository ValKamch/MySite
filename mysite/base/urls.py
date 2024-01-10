from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shopapp.urls')),
    path('req/', include('requestdataapp.urls')),
    path('myauth/', include('myauth.urls'))
]

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)