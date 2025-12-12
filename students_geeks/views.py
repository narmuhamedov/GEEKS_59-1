from django.shortcuts import render, get_object_or_404, redirect
from students_geeks.models import Student
from students_geeks.forms import StudentForm
from django.http import HttpResponse



#search
def searchStudent(request):
    query = request.GET.get('s', '')
    if query:
        student = Student.objects.filter(name__icontains=query)
    else:
        student = Student.objects.none
    return render(
        request,
        'students/student_list.html',
        {
            'student': student,
            's': query
        }
    )





#CRUD - CREATE READ UPDATE DELETE


#DELETE
def deleteStudent(request,id):
    student_id = get_object_or_404(Student, id=id)
    student_id.delete()
    return redirect('student_list')
    #return HttpResponse('Студент успешно удален!')




#UPDATE
def updateStudent(request, id):
    student_id = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student_id)
        if form.is_valid():
            form.save()
            return redirect('student_list')
            #return HttpResponse('Вы успешно обновили свои данные')
    else:
        form = StudentForm(instance=student_id)
    return render(
        request, 
            'students/student_update.html',
        {
            'form': form,
            'student_id': student_id,
        }
    )



#READ - LIST/DETAIL

def studentDetail(request, id):
    student_id = get_object_or_404(Student, id=id)
    return render(
        request,
        'students/student_detail.html',
        {
            "student_id": student_id,
        }
    )

def studentList(request):
    if request.method == 'GET':
        student = Student.objects.all().order_by('-id')
        return render(
            request,
            'students/student_list.html',
            {
                'student': student,
            }
        )



#CREATE
def createStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('student_list')
            #return HttpResponse('Вы успешно зарегистрировались ожидайте звонка!')
    else:
        form = StudentForm()
    return render(
        request,
        'students/create_student.html',
        {
            "form": form,
        }
    )

