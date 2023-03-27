from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from ks_students.models import Student
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django_tables2 import SingleTableView
from ks_students.tables import StudentTable


@method_decorator(login_required, name='dispatch')
class StudentsListView(SingleTableView):
    model = Student
    table_class = StudentTable
    template_name = 'student/students.html'


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    template_name = 'student/student_create.html'
    fields = ('surname', 'name', 'patronymic', 'bio', 'university', 'admission_year', 'phone_number',
              'email', 'communication_other', 'birth_date', 'mentor', 'photo')
    success_url = reverse_lazy('students-list')


@method_decorator(login_required, name='dispatch')
class StudentDetailView(DetailView):

    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'


@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_delete.html'
    success_url = reverse_lazy('students-list')


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):

    model = Student
    template_name = 'student/student_update.html'
    context_object_name = 'student'
    fields = ('surname', 'name', 'patronymic', 'bio', 'university', 'admission_year', 'phone_number',
              'email', 'communication_other', 'birth_date', 'mentor', 'photo')

    def get_success_url(self):
        return reverse_lazy('student-detail', kwargs={'pk': self.object.id})
