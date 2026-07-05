from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Mark, standard
from django.views.decorators.csrf import csrf_exempt
import json
def student_list(request):
    return JsonResponse({"message": "Student List API"})

def student_detail(request, student_id):
    return JsonResponse({
        "message": "Student Detail API",
        "student_id": student_id
    })
# Create your views here.
