from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"carritos", views.CarritoViewSet)
router.register(r"agencias", views.AgenciaViewSet)

#direcciones URL
urlpatterns = [     
    path('', include(router.urls))
]