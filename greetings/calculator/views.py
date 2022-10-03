from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
class AddView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2

        return Response({"msg":res})



# Create your views here.
