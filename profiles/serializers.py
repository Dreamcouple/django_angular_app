from rest_framework import serializers
from .models import profiles


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = profiles
        fields = ['id', 'date', 'qualification', 'hometown']