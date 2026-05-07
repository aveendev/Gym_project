from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .models import Player, Coach
from .serializers import PlayerSerializer , CoachSerializer
# Create your views here.
