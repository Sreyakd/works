from rest_framework import serializers
from dishapi.models import Dishes

class DishSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    category=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()

    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid price")
        return data
class DishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields="__all__"

    def validate(self,data):
        price=data.get("price")
        if price<0:
            raise serializers.ValidationError("invalid price")
        return data

