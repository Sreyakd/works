from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from dishapi.models import Dishes
from dishapi.serializer import DishSerializer,DishModelSerializer
from rest_framework import status
from rest_framework.viewsets import ViewSet




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

class DishModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        if "category" in request.query_params:

            qs=qs.filter(category__contains=request.query_params.get("category"))
        serializer=DishModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer=DishModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return  Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DishdetailModelView(APIView):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        object = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(object)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        object=Dishes.objects.get(id=id)
        serializer=DishModelSerializer(data=request.data,instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        object = Dishes.objects.get(id=id)
        serializer=DishModelSerializer(object)
        object.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)

class DishViewSetView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs = Dishes.objects.all()
        serializer = DishModelSerializer(qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self,request,*args,**kwargs):
        serializer = DishModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(object)
        return Response(data=serializer.data)

    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(data=request.data, instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        object = Dishes.objects.get(id=id)
        serializer = DishModelSerializer(object)
        object.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)


















# Create your views here.
