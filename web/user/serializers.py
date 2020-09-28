from rest_framework import serializers
from .models import User

class User_Serializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'name',
			'email',
			'phone',
			'account_type',
			'password',
			)
		model = User