from rest_framework import serializers

from users.models import User, Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'city', 'avatar', 'payments']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'city', 'avatar', 'password', ]

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            city=validated_data.get('city'),
            avatar=validated_data.get('avatar'),
            phone_number=validated_data.get('phone_number')
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детального отображения профиля пользователя"""
    payment_history = PaymentsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'payment_history']
        read_only_fields = ['payment_history']


class UserPublicSerializer(serializers.ModelSerializer):
    """Сериализатор для публичного отображения профиля пользователя"""

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']
