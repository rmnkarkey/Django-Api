from modRelation.models import Reporter,Article
from rest_framework import serializers

class modelsSerializers(serializers.ModelSerializer):
	class Meta:
		model=Reporter
		fields=('id','first_name','last_name','email')


class AotherSerializer(serializers.ModelSerializer):
	class Meta:
		model=Article
		fields=('id','headline','pub_date','reporter')