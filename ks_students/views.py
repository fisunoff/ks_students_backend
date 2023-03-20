from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from ks_students.models import Student
from mentor.models import Profile
from interaction.models import Interaction
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from ks_students import forms


class StudentsListView(ListView):
    model = Student

    def get(self, request, *args, **kwargs):
        students = self.get_queryset().all()
        return render(request, self.template_name, {'students_list': students})


@method_decorator(login_required, name='dispatch')
class StudentCreateView(CreateView):
    model = Student
    template_name = 'student/student_create.html'
    fields = ('surname', 'name', 'patronymic', 'bio', 'university', 'admission_year', 'phone_number',
              'email', 'communication_other', 'birth_date', 'mentor', 'photo')
    success_url = reverse_lazy('students_list')


class StudentDetailView(DetailView):

    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'



@method_decorator(login_required, name='dispatch')
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_delete.html'
    success_url = reverse_lazy('students_list')


@method_decorator(login_required, name='dispatch')
class StudentUpdateView(UpdateView):

    model = Student
    template_name = 'student/student_update.html'
    context_object_name = 'student'
    fields = ('surname', 'name', 'patronymic', 'bio', 'university', 'admission_year', 'phone_number',
              'email', 'communication_other', 'birth_date', 'mentor', 'photo')

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.id})
