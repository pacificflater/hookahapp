from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

app_name = 'sklad'

router = routers.DefaultRouter()
router.register(r'manufacturer', views.Manufacturers, basename='Manufacturer')
router.register(r'flavour', views.FlavoursView, basename='Flavour')
router.register(r'mix', views.MixesView)
router.register(r'membership', views.MembershipView)
router.register(r'flavour_types', views.FlavourTypeView)
router.register(r'manufacturer_type', views.ManufacturerTypeView)
router.register(r'bowls', views.BowlView)
router.register(r'bowl_types', views.BowlTypeView)
router.register(r'mixes_in_stock', views.MixesInStockView)
# router.register(r'available_mixes', views.AvailableMixesView, basename='AvailableMixes')


urlpatterns = [
    url(r'^$', views.index),
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    url(r'^(?P<path>.*)/$', views.index),
]
