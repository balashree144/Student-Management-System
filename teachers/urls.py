from django.urls import path
from . import views
from .views import TeachersView

urlpatterns = [
    path('teachers/', views.add_teacher, name='add_teacher'),
    path('update/<int:teacher_id>/', views.update_teacher, name='update_teacher'),
    path('delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('', TeachersView.as_view(), name='teachers')
]