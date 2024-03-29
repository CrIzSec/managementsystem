
from django.contrib import admin
from django.urls import path, include
from core.views import index, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__reload__/', include("django_browser_reload.urls")),
    path('', include("dashboard.urls")),
    path('', include("product.urls")),
    path('', include("tablelist.urls")),
    path('', include("notification.urls")),
    path('', include("message.urls")),
    path('', index, name='login'),
    path('logout/', logout_user, name='logout'),
]
