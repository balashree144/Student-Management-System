from django.urls import path
from . import views
from .views import StudentView

urlpatterns = [
    path("", StudentView.as_view(), name="students"),
    path("<int:id>/", StudentView.as_view(), name="student"),

    path("students/add/", views.add_student, name="add_student"),
    path("update/<int:student_id>/", views.update_student, name="update_student"),
    path("delete/<int:student_id>/", views.delete_student, name="delete_student"),
]