from rest_framework import generics
from .serializers import modelsSerializers, AotherSerializer
from modRelation.models import Reporter,Article
from rest_framework.viewsets import ModelViewSet
class Rep(ModelViewSet):
	queryset=Reporter.objects.all()
	serializer_class=modelsSerializers

class Ar(ModelViewSet):
	queryset=Article.objects.all()
	serializer_class=AotherSerializer


