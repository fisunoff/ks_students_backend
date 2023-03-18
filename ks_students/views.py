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
              'email', 'communication_other', 'birth_date', 'mentor')
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
              'email', 'communication_other', 'birth_date', 'mentor')

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'pk': self.object.id})



class StudentListView(ListView):
    model = Student

    def get(self, request, *args, **kwargs):
        student = Student.objects.get(pk=kwargs['student_id'])
        initial_data = {}
        if student:
            initial_data = {'name': student.name, 'surname': student.surname, 'patronymic': student.patronymic,
                            'bio': student.bio, 'university': student.university,
                            'admission_year': student.admission_year, 'phone_number': student.phone_number,
                            'email': student.email, 'communication_other': student.communication_other,
                            'birth_date': student.birth_date, 'mentor': student.mentor}
        form = forms.StudentForm(initial_data, instance=student)

        mentors = Profile.objects.all()
        interactions = Interaction.objects.filter(student=kwargs['student_id'])

        return render(request, self.template_name, {'student': student if student else False,
                                                    'mentors': mentors, 'interactions_list': interactions,
                                                    'form': form})
