from rest_framework import authentication, permissions, parsers, status, exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from metropolis import settings


class APIVersion(APIView):
    def get(self, request):
        return Response({'version': settings.API_VERSION})
