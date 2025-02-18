from  rest_framework import serializers
from .models import Text


class LoadImageSerializer(serializers.Serializer):
    url = serializers.URLField()


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'
