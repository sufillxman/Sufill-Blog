from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # Username check logic
        if data.get('username'):
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('Username is already taken.')
        
        # Sahi jagah return karo (Dead code hata diya)
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data