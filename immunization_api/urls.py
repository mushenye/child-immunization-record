from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'children', views.ChildViewSet)
router.register(r'caregiver', views.CaregiverViewset)
router.register(r'vaccines', views.VaccineViewSet)
router.register(r'immunization-schedules', views.ImmunizationScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
