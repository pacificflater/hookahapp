from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views

app_name = 'sklad'

router = routers.DefaultRouter()
router.register(r'manufacturers', views.Manufacturers)
router.register(r'flavours', views.FlavoursView)
router.register(r'mixes', views.MixesView)
router.register(r'membership', views.MembershipView)


urlpatterns = [
    # path('', views.index,  name='index', ),
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    # path('in_stock/', views.InStockView.as_view(), name='in_stock'),
    # path('manufacturers/', views.Manufacturers.as_view(), name='manufacturers'),
    # path('manufacturers/<int:pk>/manufacturer_card/', views.ManufacturerCardView.as_view(), name='manufacturer_card'),
    # path('manufacturers/new', views.manufacturer_form, name='manufacturer_form'),
    # path('manufacturers/create', views.manufacturer_create, name='manufacturer_create'),
    # path('manufacturers/<int:manufacturer_id>/delete', views.manufacturer_delete, name='manufacturer_delete'),
    # path('manufacturers/<int:manufacturer_id>/flavour_list/new/', views.flavour_add, name='flavour_add'),
    # path('manufacturers/<int:manufacturer_id>/flavour_list/form/', views.flavour_form, name='flavour_form'),
    # path('manufacturers/<int:manufacturer_id>/flavour_list/<int:flavour_id>', views.flavour_card, name="flavour_card"),
    # path('manufacturers/<int:manufacturer_id>/flavour_list/<int:flavour_id>/delete/', views.flavour_delete, name="flavour_delete")
]
