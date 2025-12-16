from django.urls import path
from students_geeks.views import CreateStudentView, StudentListView,StudentDetailView, UpdateStudentView,DeleteStudentView, SearchView

urlpatterns = [
    path('create_studens/', CreateStudentView.as_view(), name='create_student'),
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('student_list/<int:id>/', StudentDetailView.as_view(), name='student_detail'),
    path('student_list/<int:id>/update/', UpdateStudentView.as_view(), name='updateStudent'),
    path('student_list/<int:id>/delete/', DeleteStudentView.as_view(), name='deleteStudent'),
    path('search/', SearchView.as_view(), name='search'),
]