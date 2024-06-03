from django.shortcuts import render
from django.views.generic import TemplateView 

# Create your views here.

from rest_framework import viewsets
from .serializers import QuestionsSerializers
from .models import Questions




class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers


class index(TemplateView):
    template_name = "index.html"