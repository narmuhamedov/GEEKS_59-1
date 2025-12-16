from django.shortcuts import render, get_object_or_404, redirect
from students_geeks.models import Student
from students_geeks.forms import StudentForm
from django.http import HttpResponse
from django.views import generic


#search
class SearchView(generic.View):
    def get(self, request):
        query = request.GET.get('s', '')
        if query:
            student = Student.objects.filter(name__icontains=query)
        else:
            student = Student.objects.none
        context_object_name = {
             'student': student,
             's': query,
        }
        return render(
            request,
            template_name='students/student_list.html',
            context=context_object_name
        )



# def searchStudent(request):
#     query = request.GET.get('s', '')
#     if query:
#         student = Student.objects.filter(name__icontains=query)
#     else:
#         student = Student.objects.none
#     return render(
#         request,
#         'students/student_list.html',
#         {
#             'student': student,
#             's': query
#         }
#     )





#CRUD - CREATE READ UPDATE DELETE


#DELETE
class DeleteStudentView(generic.DeleteView):
    template_name = 'students/confirm_delete.html'
    model = Student
    context_object_name = 'student_id'
    success_url = '/student_list/'


    def get_object(self, **kwargs):
        student_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=student_id)



# def deleteStudent(request,id):
#     student_id = get_object_or_404(Student, id=id)
#     student_id.delete()
#     return redirect('student_list')
#     #return HttpResponse('Студент успешно удален!')




#UPDATE
class UpdateStudentView(generic.UpdateView):
    template_name = 'students/student_update.html'
    form_class = StudentForm
    success_url = '/student_list/'
    model = Student

    def get_object(self, **kwargs):
        student_id = self.kwargs.get('id')
        return get_object_or_404(self.model, id=student_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateStudentView, self).form_valid(form=form)
        
        



# def updateStudent(request, id):
#     student_id = get_object_or_404(Student, id=id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student_id)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#             #return HttpResponse('Вы успешно обновили свои данные')
#     else:
#         form = StudentForm(instance=student_id)
#     return render(
#         request, 
#             'students/student_update.html',
#         {
#             'form': form,
#             'student_id': student_id,
#         }
#     )



#READ - LIST/DETAIL

class StudentDetailView(generic.DetailView):
    template_name = 'students/student_detail.html'
    model = Student
    context_object_name = 'student_id'


    def get_object(self, **kwargs):
        student_id = self.kwargs.get("id")
        return get_object_or_404(self.model, id=student_id)


# def studentDetail(request, id):
#     student_id = get_object_or_404(Student, id=id)
#     return render(
#         request,
#         'students/student_detail.html',
#         {
#             "student_id": student_id,
#         }
#     )


class StudentListView(generic.ListView):
    template_name = 'students/student_list.html'
    model = Student
    context_object_name = 'student'


# def studentList(request):
#     if request.method == 'GET':
#         student = Student.objects.all().order_by('-id')
#         return render(
#             request,
#             'students/student_list.html',
#             {
#                 'student': student,
#             }
#         )



#CREATE

class CreateStudentView(generic.CreateView):
    template_name = 'students/create_student.html'
    form_class = StudentForm
    success_url = '/student_list/'



# def createStudent(request):
#     if request.method == "POST":
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#             #return HttpResponse('Вы успешно зарегистрировались ожидайте звонка!')
#     else:
#         form = StudentForm()
#     return render(
#         request,
#         'students/create_student.html',
#         {
#             "form": form,
#         }
#     )

