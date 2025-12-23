from rest_framework.viewsets import ModelViewSet
from members.models import Member
from members.serializers import MemberSerializers, MemberCreateSerializers
from api.custom_permissions import IsLibrarian

class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [IsLibrarian]

    def get_serializer_class(self):
        if self.action == 'create':
            return MemberCreateSerializers
        return MemberSerializers
