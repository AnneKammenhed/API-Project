from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='follower.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'followed', 'created_at', 'followed_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
