from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('immunization_api.urls')),
    path ('user/', include('account_manager.urls'))
]
