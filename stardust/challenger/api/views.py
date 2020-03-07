from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ChallengeSerializer


class ChallengeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChallengeSerializer(data=request.data, owner=str(request.user))
        data = {}
        if serializer.is_valid():
            challenge = serializer.save()
            data['response'] = 'Challenge successfully created.'
            data['name'] = challenge.name
            data['owner'] = challenge.owner
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
