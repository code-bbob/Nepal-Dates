from .models import Profile,ProfileImages
from rest_framework import serializers

class ProfilesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImages
        fields= '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    images = ProfilesImageSerializer(many=True)
    class Meta:
        model= Profile
        fields = ['images']