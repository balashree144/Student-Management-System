from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Students
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class StudentView(View):

    # GET
    def get(self, request, id=None):
        try:
            if id:
                try:
                    student = Students.objects.get(id=id)
                    data = {
                        "id": student.id,
                        "name": student.name,
                        "age": student.age,
                        "course": student.course
                    }
                    return JsonResponse(data)
                except Students.DoesNotExist:
                    return JsonResponse({"message": "Student not found"}, status=404)

            students = Students.objects.all()
            data = []

            for student in students:
                data.append({
                    "id": student.id,
                    "name": student.name,
                    "age": student.age,
                    "course": student.course
                })

            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)

    # POST
@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data = json.loads(request.body)

        student = Students.objects.create(
            name=data.get("name"),
            age=data.get("age"),
            course=data.get("course")
        )

        return JsonResponse({
            "message": "Student added successfully.",
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "course": student.course
        })

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def update_student(request, student_id):
    if request.method == "PUT":
        data = json.loads(request.body)

        try:
            student = Students.objects.get(id=student_id)

            student.name = data.get("name", student.name)
            student.age = data.get("age", student.age)
            student.course = data.get("course", student.course)

            student.save()

            return JsonResponse({
                "message": "Student updated successfully.",
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "course": student.course
            })

        except Students.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def delete_student(request, student_id):
    if request.method == 'DELETE':
        try:
            student_obj = Students.objects.get(id=student_id)
            student_obj.delete()
            return JsonResponse({'message': 'Student deleted successfully.'})
        except Students.DoesNotExist:
            return JsonResponse({'error': 'Student not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)           
   