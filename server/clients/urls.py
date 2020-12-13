from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'clients'

router = routers.DefaultRouter()
router.register('deals', views.DealsViewSet)

urlpatterns = [
    path('api/', include((router.urls, 'app_name'))),
]
