from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .serializers import ChallengeSerializer


class ChallengeView(APIView):
    class BurstRateThrottle(UserRateThrottle):
        scope = 'challenge_user_burst'

    class SustainedRateThrottle(UserRateThrottle):
        scope = 'challenge_user_sustained'

    permission_classes = [IsAuthenticated]
    throttle_classes = [SustainedRateThrottle, BurstRateThrottle]

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
