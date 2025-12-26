from rest_framework import serializers
from members.models import Member

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'email', 'address', 'phone')
class MemberCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'first_name', 'last_name', 'email', 'address', 'phone', 'password')
    def create(self, validated_data):
        member = Member.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            address=validated_data.get('address', None),
            phone=validated_data.get('phone', None),
        )
        return member
