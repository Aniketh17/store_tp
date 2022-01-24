from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.apps.store.urls', namespace='store')),
    path('checkout/', include('core.apps.checkout.urls', namespace='checkout')),
    path('basket/', include('core.apps.basket.urls', namespace='basket')),
    path('orders/', include('core.apps.orders.urls', namespace='orders')),
    path('account/', include('core.apps.account.urls', namespace='account')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
