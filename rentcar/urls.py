from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('shop/', include('shop.urls', namespace='cars')),
    path('blog/', include('blog.urls', namespace='posts')),
    path('profile/', include('users.urls', namespace='profile')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
