from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='posts')),
    path('shop/', include('shop.urls', namespace='cars')),
    path('', include('pages.urls', namespace='pages')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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