from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^files/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
