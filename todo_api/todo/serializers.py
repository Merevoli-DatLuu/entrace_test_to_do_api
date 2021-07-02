from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': False},
            'description': {'required': False},
            'date_of_completion': {'required': False},
            'user_id': {'required': False}
        }

    def validate(self, attrs):
        return super().validate(attrs)

    def update(self, instance, validated_data):

        # Không thay đổi user_id
        if validated_data.get('user_id'):
            validated_data['user_id'] = getattr(instance, 'user_id')

        # Không có những field này thì giữ nguyên
        for field_name in ('name', 'description', 'date_of_completion'):
            if not validated_data.get(field_name):
                validated_data[field_name] = getattr(instance, field_name)

        super().update(instance, validated_data)

        return instance

    

class TodoAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['user_id']
        extra_kwargs = {
            'user_id': {'required': True},
        }



