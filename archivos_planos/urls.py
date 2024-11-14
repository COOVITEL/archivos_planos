from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('colpensiones/', include('formatos.urls')),
    path('', include('account.urls')),
    path('__reload__/', include('django_browser_reload.urls'))
]
