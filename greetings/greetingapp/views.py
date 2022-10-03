from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

class GreetingView(APIView):
    def get(self,request,*args,**kwargs):


        cur_date=datetime.now()
        cur_hour=cur_date.hour

        greeting=""
        if cur_hour<12:
            greeting="goodmorning"

        elif cur_hour<18:
            greeting = "goodafternoon"

        elif cur_hour<24:
            greeting = "goodevening"



        return Response({"msg":greeting})


# Create your views here.
