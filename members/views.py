from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin, ListModelMixin
from members.models import Member
from members.serializers import MemberSerializers, MemberCreateSerializers

class MemberViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MemberSerializers
        return MemberCreateSerializers