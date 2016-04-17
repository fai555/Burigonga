from rest_framework import serializers

from hello.models import Task
from hello.models import WaterParticle


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')

class WaterParticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = WaterParticle
		fields = ('user', 'deviceID', 'ph', 'temperature', 'orp', 'dateTime', 'geoLocation')
