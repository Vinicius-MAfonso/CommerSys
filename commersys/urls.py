from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('comercial/', include('comercial.urls')),
    path('estoque/', include('estoque.urls')),
    path('accounts/', include('accounts.urls')),
]