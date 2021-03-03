from rest_framework import serializers
from .models import Ad, Advertiser, Click, View


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields =('name', )


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields ="__all__"


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields ="__all__"


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields ="__all__"