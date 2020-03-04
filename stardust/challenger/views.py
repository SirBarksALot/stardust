from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def index(request):
    return render(request, 'challenger/index.html')
