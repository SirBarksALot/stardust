from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser

from utils.ssl_check import Ssl


class CheckView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [FormParser]

    def get(self, request):
        data = dict()

        domain = request.data.get('name')
        certificate = Ssl(domain)

        data['response'] = f'{domain} successfully checked.'
        data['domain name'] = domain
        data['output'] = certificate.check_ssl()

        return Response(data, status=status.HTTP_200_OK)
