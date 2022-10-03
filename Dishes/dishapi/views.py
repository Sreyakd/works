from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from dishapi.models import Dishes
from dishapi.serializer import DishSerializer
from rest_framework import status


class DishesView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializer=DishSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def post(self,request,*args,**kwargs):
        serializer=DishSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Dishes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DishdetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serilaizer=DishSerializer(qs)
        return Response(data=serilaizer.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.filter(id=id)
        serializer=DishSerializer(data=request.data)
        if serializer.is_valid():
            # instance.name=serializer.validated_data.get("name")
            # instance.category=serializer.validated_data.get("category")
            # instance.price=serializer.validated_data.get("price")
            # instance.rating=serializer.validated_data.get("rating")
            # instance.save()
            instance.update(**serializer.validated_data)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializer=DishSerializer(instance)
        instance.delete()
        return Response({"msg":"dish deleted"},status=status.HTTP_204_NO_CONTENT)


# Create your views here.
