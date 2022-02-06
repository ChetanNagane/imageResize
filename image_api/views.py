from django.shortcuts import render
from rest_framework.views import APIView
from .models import record
from .serializer import recordSerializer
from rest_framework.response import Response

# Create your views here.
class records(APIView):

    def post(self, request):
        serializer = recordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error_messages)

    def get(self, request):
        records = record.objects.all()
        serializer = recordSerializer(records, many=True)
        return Response(serializer.data)
