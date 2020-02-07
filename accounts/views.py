from rest_framework import viewsets
from rest_framework.mixins import (CreateModelMixin,
                                   ListModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin,
                                   RetrieveModelMixin)
from rest_framework.permissions import IsAuthenticated

from .models import UserAccount
from .serializers import UserAccountSerializer


class AccountViewSet(ListModelMixin,
                     CreateModelMixin,
                     RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserAccountSerializer

    def get_queryset(self):
        return UserAccount.objects.filter(user=self.request.user)
