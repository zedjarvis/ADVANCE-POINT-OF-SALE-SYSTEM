# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Cedrouseroll
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from apps.authentication import views


handler400 = 'apps.authentication.views.handler400'
handler403 = 'apps.authentication.views.handler403'
handler404 = 'apps.authentication.views.handler404'
handler500 = 'apps.authentication.views.handler500'


urlpatterns = [
    path('admin/login/', views.handler403),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.authentication.urls')),
    path('pos/', include('apps.pos.urls')),
    path('restful_api/', include('apps.crud.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
