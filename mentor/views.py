from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils import timezone
from mentor.models import Profile
from django_tables2 import SingleTableView
from mentor.tables import MentorTable


@method_decorator(login_required, name='dispatch')
class MentorsListView(SingleTableView):
    model = Profile
    table_class = MentorTable
    template_name = 'mentor/mentors.html'

@method_decorator(login_required, name='dispatch')
class MentorDetailView(DetailView):
    model = Profile
    template_name = 'mentor/detail.html'
    context_object_name = 'mentor'


@method_decorator(login_required, name='dispatch')
class MentorUpdateView(UpdateView):
    model = Profile
    template_name = 'mentor/update.html'
    context_object_name = 'mentor'
    fields = ('surname', 'name', 'patronymic', 'bio', 'birth_date', 'position', 'mentor')

    def get_success_url(self):
        self.object.time_edit = timezone.now()
        self.object.save()
        return reverse_lazy('mentor-detail', kwargs={'pk': self.object.id})
