from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer
from . import serializers





@api_view(['GET','POST'])
def get_all_supers(request):
   if request.method == 'GET':
      super_param = request.query_params.get('type')
      
      super = Super.objects.all()

      custom_response_dictionary = {}

      if super_param == 'hero':
         super = super.filter(super_type__type='hero')
         hero_serializer = SuperSerializer(super,many=True)
         return Response(hero_serializer.data)
      elif super_param == 'villain':
         super = super.filter(super_type__type='villain')
         villain_serializer = SuperSerializer(super,many=True)
         return Response(villain_serializer.data)
      else:
      
         for index in super:
            hero = Super.objects.filter(super_type_id=1)
            villain = Super.objects.filter(super_type_id=2)

            hero_serializer = SuperSerializer(hero, many=True)
            villain_serializer = SuperSerializer(villain, many=True)\

         

         custom_response_dictionary['affiliation'] = {
            "Heroes" : hero_serializer.data ,
            "Villains" : villain_serializer.data

         }
      
      return Response(custom_response_dictionary)
  
      
   elif request.method == 'POST':
       serializer = SuperSerializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])
def super_detail(request,pk):
   super = get_object_or_404(Super,pk=pk)
   if request.method == 'GET':
      serializer = SuperSerializer(super);
      return Response(serializer.data)
   elif request.method =='PUT':
      serializer = SuperSerializer(super, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response(serializer.data)
   elif request.method == 'DELETE':
      super.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)






