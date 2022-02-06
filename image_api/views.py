from django.shortcuts import render
from rest_framework.views import APIView
from .models import record
from .serializer import recordSerializer
from rest_framework.response import Response
import django_rq
from .tasks import imageResize

# Create your views here.
class records(APIView):

    def post(self, request):
        serializer = recordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            queue = django_rq.get_queue('low')
            queue.enqueue(imageResize,serializer.data['id'])
            return Response(serializer.data)
        else:
            return Response(serializer.error_messages)

    def get(self, request):
        records = record.objects.all()
        serializer = recordSerializer(records, many=True)
        return Response(serializer.data)
