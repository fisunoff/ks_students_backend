from django.shortcuts import render

# Create your views here.
from djangoProject_students.edited_views import CreateViewDecorated, SingleTableViewDecorated, DetailViewDecorated,\
    DeleteViewDecorated, UpdateViewDecorated
from ks_students.models import Student
from django.urls import reverse_lazy
from ks_students.tables import StudentTable


class StudentsListView(SingleTableViewDecorated):
    model = Student
    table_class = StudentTable
    template_name = 'student/students.html'


class StudentCreateView(CreateViewDecorated):
    model = Student
    template_name = 'student/student_create.html'
    fields = ('surname', 'name', 'patronymic', 'bio', 'university', 'admission_year', 'phone_number',
              'email', 'communication_other', 'birth_date', 'mentor', 'photo')
    success_url = reverse_lazy('students-list')


class StudentDetailView(DetailViewDecorated):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'


class StudentDeleteView(DeleteViewDecorated):
    model = Student
    template_name = 'student/student_delete.html'
    success_url = reverse_lazy('students-list')


class StudentUpdateView(UpdateViewDecorated):

    model = Student
    template_name = 'student/student_update.html'
    context_object_name = 'student'
    fields = ('surname', 'name', 'patronymic', 'bio', 'university', 'admission_year', 'phone_number',
              'email', 'communication_other', 'birth_date', 'mentor', 'photo')

    def get_success_url(self):
        return reverse_lazy('student-detail', kwargs={'pk': self.object.id})
