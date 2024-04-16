from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, CharField


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
