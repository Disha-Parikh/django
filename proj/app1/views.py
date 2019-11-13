# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.


class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data  = request.data
        print ("data", data)
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            print ("if")
            serializer.save()
        else:
            print ("pass")
        return Response(serializer.data)


