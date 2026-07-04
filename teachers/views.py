from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Teachers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class TeachersView(View):

    # GET
    def get(self, request, id=None):
        try:
            if id:
                try:
                    teacher = Teachers.objects.get(id=id)
                    data = {
                        "id": teacher.id,
                        "name": teacher.name,
                        "age": teacher.age,
                        "course": teacher.course
                    }
                    return JsonResponse(data)
                except Teachers.DoesNotExist:
                    return JsonResponse({"message": "Teacher not found"}, status=404)

            teacher = Teachers.objects.all()
            data = []

            for teacher in teacher:
                data.append({
                    "id": teacher.id,
                    "name": teacher.name,
                    "age": teacher.age,
                    "course": teacher.course
                })

            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)

    # POST
@csrf_exempt
def add_teacher(request):
    if request.method == "POST":
        data = json.loads(request.body)

        teacher = Teachers.objects.create(
            name=data.get("name"),
            age=data.get("age"),
            course=data.get("course")
        )

        return JsonResponse({
            "message": "Teacher added successfully.",
            "id": teacher.id,
            "name": teacher.name,
            "age": teacher.age,
            "course": teacher.course
        })

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def update_teacher(request, teacher_id):
    if request.method == "PUT":
        data = json.loads(request.body)

        try:
            teacher = Teachers.objects.get(id=teacher_id)

            teacher.name = data.get("name", teacher.name)
            teacher.age = data.get("age", teacher.age)
            teacher.course = data.get("course", teacher.course)

            teacher.save()

            return JsonResponse({
                "message": "Teacher updated successfully.",
                "id": teacher.id,
                "name": teacher.name,
                "age": teacher.age,
                "course": teacher.course
            })

        except Teachers.DoesNotExist:
            return JsonResponse({"error": "Teacher not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=400)

@csrf_exempt
def delete_teacher(request, teacher_id):
    if request.method == 'DELETE':
        try:
            teacher_obj = Teachers.objects.get(id=teacher_id)
            teacher_obj.delete()
            return JsonResponse({'message': 'Teacher deleted successfully.'})
        except Teachers.DoesNotExist:
            return JsonResponse({'error': 'Teacher not found.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)           
