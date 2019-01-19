from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("boards.urls")),
    path('auth/', include("djoser.urls")),
    path('auth/', include("djoser.urls.authtoken")),
    path('auth/', include("djoser.urls.jwt"))
]
