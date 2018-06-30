from rest_framework import serializers
from karikatura.models import ImageModel



class karikaturaSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImageModel
		fields = [
			'get_image',
			'name',
			'pk',
		]