from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Marks, standard
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
