from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from mentor.models import Profile


class MentorsListView(ListView):
    model = Profile

    template_name = 'mentor/mentors.html'
    context_object_name = 'mentors'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MentorsListView, self).get_context_data(**kwargs)
        mentors = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(mentors, self.paginate_by)
        try:
            mentors = paginator.page(page)
        except PageNotAnInteger:
            mentors = paginator.page(1)
        except EmptyPage:
            mentors = paginator.page(paginator.num_pages)
        context['mentors'] = mentors
        return context


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
        return reverse_lazy('mentor_detail', kwargs={'pk': self.object.id})
