from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view, logout_view
urlpatterns = []

urlpatterns = [
    url(r'^admin/', admin.site.urls, name = 'admin'),
    url(r'^posts/', include("posts.urls", namespace = 'posts')),
    url(r'^logout/', logout_view, name = 'logout'),
    url(r'^$', login_view, name='login'),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
