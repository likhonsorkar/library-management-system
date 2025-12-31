from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin, ListModelMixin
from members.models import Member
from members.serializers import MemberSerializers, MemberCreateSerializers
from django.http import HttpResponse
from django.views import View


class MemberViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MemberSerializers
        return MemberCreateSerializers

class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
