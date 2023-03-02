from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from api.urls import router_1_0_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_1_0_3.urls)),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/v1/', include('djoser.urls.jwt')),
]
