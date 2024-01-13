from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('req/', include('requestdataapp.urls')),
    #path('myauth/', include('myauth.urls'))
    path('api/', include('myapiapp.urls'))
]

urlpatterns += i18n_patterns(
    path('myauth/', include('myauth.urls')),
    path('shop/', include('shopapp.urls')),
)

if settings.DEBUG:
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

urlpatterns.extend(
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
urlpatterns.append(
    path("__debug__/", include("debug_toolbar.urls"))
)