from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from djangoProject_students.edited_views import SingleTableViewDecorated, DetailViewDecorated,\
    UpdateViewDecorated
from mentor.models import Profile
from mentor.tables import MentorTable


class MentorsListView(SingleTableViewDecorated):
    model = Profile
    table_class = MentorTable
    template_name = 'mentor/mentors.html'


class MentorDetailView(DetailViewDecorated):
    model = Profile
    template_name = 'mentor/detail.html'
    context_object_name = 'mentor'


class MentorUpdateView(UpdateViewDecorated):
    model = Profile
    template_name = 'mentor/update.html'
    context_object_name = 'mentor'
    fields = ('surname', 'name', 'patronymic', 'bio', 'birth_date', 'position', 'mentor')

    def get_success_url(self):
        self.object.time_edit = timezone.now()
        self.object.save()
        return reverse_lazy('mentor-detail', kwargs={'pk': self.object.id})
