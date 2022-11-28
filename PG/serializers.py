from rest_framework import serializers

from .models import *


class PGSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ParametricGraph
        fields = "__all__"


class LayerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Layer
        fields = "__all__"


class NodeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Node
        fields = "__all__"

class AllSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    Layer = PGSerializer(read_only=True)
    class Meta:
        model = Layer
        fields = "__all__"