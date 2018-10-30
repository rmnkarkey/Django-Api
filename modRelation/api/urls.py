from rest_framework import routers
from .serializers import modelsSerializers, AotherSerializer
from modRelation.models import Reporter,Article
from . import views
from django.urls import path,include

router=routers.DefaultRouter()
router.register('api/',views.Rep)
router.register('apis/',views.Ar)

urlpatterns=[
	path('',include(router.urls))
]