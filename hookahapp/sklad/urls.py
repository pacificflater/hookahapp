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
    path('api/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
]
