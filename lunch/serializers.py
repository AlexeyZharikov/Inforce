from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Restaurant, Menu, Vote
from datetime import date


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'date', 'items']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['menu']

    def validate(self, attrs):
        user = self.context['request'].user
        if Vote.objects.filter(employee=user, date=date.today()).exists():
            raise serializers.ValidationError("You have already voted today.")
        return attrs
