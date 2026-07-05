from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Students
from .serializers import StudentSerializer
import json

@method_decorator(csrf_exempt, name='dispatch')
class StudentView(View):

    # GET
    def get(self, request, id=None):
        if id:
            try:
                student = Students.objects.get(id=id)
                serializer = StudentSerializer(student)
                return JsonResponse(serializer.data)
            except Students.DoesNotExist:
                return JsonResponse({"message": "Student not found"}, status=404)

        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)


# POST
@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data = json.loads(request.body)

        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=400)


# PUT
@csrf_exempt
def update_student(request, student_id):
    if request.method == "PUT":
        try:
            student = Students.objects.get(id=student_id)
        except Students.DoesNotExist:
            return JsonResponse({"message": "Student not found"}, status=404)

        data = json.loads(request.body)

        serializer = StudentSerializer(student, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=400)


# DELETE
@csrf_exempt
def delete_student(request, student_id):
    if request.method == "DELETE":
        try:
            student = Students.objects.get(id=student_id)
            student.delete()
            return JsonResponse({"message": "Student deleted successfully"})
        except Students.DoesNotExist:
            return JsonResponse({"message": "Student not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=400)