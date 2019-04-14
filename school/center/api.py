from rest_framework import viewsets, permissions
from .models import *
from.serializers import loginSerializers

class loginViewSet(viewsets.ModelViewSet):
	queryset=Login.objects.all()
	permission_classes=[permissions.AllowAny]
	serializer_class=loginSerializers
