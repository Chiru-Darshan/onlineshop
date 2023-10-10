from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),

    # local paths
    path(_('cart/'), include('cart.urls', namespace='cart')),
    path(_('rosetta/'), include('rosetta.urls')),
    path(_('orders/'), include('orders.urls', namespace='orders')),
    path(_('payment/'), include('payment.urls', namespace='payment')),
    path(_('coupons/'), include('coupons.urls', namespace='coupons')),
    path(_(''), include('shop.urls', namespace='shop')),
)
    
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)