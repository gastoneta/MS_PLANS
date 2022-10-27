from django.shortcuts import render
from rest_framework import viewsets
from .models import Coupon
from .serializers import CouponSerializer
from rest_framework.response import Response

# Create your views here.

class CouponViewSet(viewsets.ViewSet):

    def list(self, request):

        code = request.query_params.get('code')
      
        if code:
            queryset = Coupon.objects.filter(code = code)
        else:
            queryset = Coupon.objects.all()


        serializer = CouponSerializer(queryset, many=True)


        return Response(serializer.data) 

        