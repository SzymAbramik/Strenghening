from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("home.urls")),
    path('diet/', include("diet.urls")),
    path('admin/', admin.site.urls),
    path('account/', include("login.urls")),
    path('training/', include("training.urls")),
    path('forum/', include("forum.urls")),
    path('bmicalc/', include("bmicalc.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)