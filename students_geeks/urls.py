from django.urls import path
from students_geeks.views import createStudent, studentList,studentDetail, updateStudent,deleteStudent, searchStudent

urlpatterns = [
    path('create_studens/', createStudent, name='create_student'),
    path('student_list/', studentList, name='student_list'),
    path('student_list/<int:id>/', studentDetail, name='student_detail'),
    path('student_list/<int:id>/update/', updateStudent, name='updateStudent'),
    path('student_list/<int:id>/delete/', deleteStudent, name='deleteStudent'),
    path('search/', searchStudent, name='search'),
]