from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import super_type
from .serializers import SuperSerializer
from super_types import serializers












@api_view(['GET'])
def get_all_supers(request):
   return Response('ok')