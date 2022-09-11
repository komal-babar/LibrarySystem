from django.shortcuts import render
from email.policy import HTTP
from urllib import response
from django import http
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from .serializers import BookSerializer
from .models import BookData
from django.shortcuts import get_object_or_404

# Create your views here.
class Bookview(APIView):
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,id=None):
        if id:
            std=BookData.objects.get(id=id)
            serializer= BookSerializer(std)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        std=BookData.objects.all()
        serializer=BookSerializer(std,many=True)
        return Response({"staus":"success","data":serializer.data},status=status.HTTP_200_OK)     
    def delete(self, request, id=None):
        std= get_object_or_404(BookData, id=id)
        std.delete()
        return Response({"status": "success", "data": "Item Deleted"})
    def patch(self, request, id=None):
        std= BookData.objects.get(id=id)
        serializer = BookSerializer(std, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})             


