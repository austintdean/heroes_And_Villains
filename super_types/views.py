from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import type
from .serializers import super_typeSerializer
from super_types import serializers



