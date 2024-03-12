from rest_framework import serializers
from users.models import User, Payment


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'phone', 'avatar', 'country', 'role']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["pay_date", "money", "pay_method", "user", "pay_course", "pay_lesson"]
