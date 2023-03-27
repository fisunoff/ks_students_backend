from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils import timezone
from interaction.models import Interaction
from django_tables2 import SingleTableView
from interaction.tables import InteractionTable


@method_decorator(login_required, name='dispatch')
class InteractionsListView(SingleTableView):
    model = Interaction
    template_name = 'interaction/interactions.html'
    table_class = InteractionTable


@method_decorator(login_required, name='dispatch')
class InteractionCreateView(CreateView):
    model = Interaction
    template_name = 'interaction/create.html'
    fields = ('interaction_name', 'description', 'type', 'mentor', 'student', 'start_date', 'end_date', 'status',
              'tags', 'file')
    success_url = reverse_lazy('interactions-list')

    def get_initial(self):
        initial_data = {}
        for i in ['interaction_name', 'student', 'description', 'type', 'mentor', 'start_date', 'end_date',
                  'status', 'tags']:
            initial_data[i] = self.request.GET.get(i)
        tags_request = self.request.GET.get('tags')
        if tags_request:
            initial_data['tags'] = list(map(int, self.request.GET.get('tags').split(",")))
        return initial_data


@method_decorator(login_required, name='dispatch')
class InteractionDetailView(DetailView):
    model = Interaction
    template_name = 'interaction/detail.html'
    context_object_name = 'interaction'

    def get_context_data(self, **kwargs):
        context = super(InteractionDetailView, self).get_context_data(**kwargs)
        context['filename'] = self.object.get_file_name()
        tags = ",".join([str(i.id) for i in self.object.tags.all()])
        context['to_copy'] = f"?interaction_name={self.object.interaction_name}&description={self.object.description}" \
                             f"&type={self.object.type.id if self.object.type else None}" \
                             f"&mentor={self.object.mentor.id if self.object.mentor else None}" \
                             f"&student={self.object.student.id if self.object.student else None}" \
                             f"&start_date={self.object.start_date}&end_date={self.object.end_date}" \
                             f"&status={self.object.status.id if self.object.status else None}" \
                             f"&tags={tags}"
        return context


@method_decorator(login_required, name='dispatch')
class InteractionDeleteView(DeleteView):
    model = Interaction
    template_name = 'interaction/delete.html'
    success_url = reverse_lazy('interactions-list')


@method_decorator(login_required, name='dispatch')
class InteractionUpdateView(UpdateView):

    model = Interaction
    template_name = 'interaction/update.html'
    context_object_name = 'interaction'
    fields = ('interaction_name', 'description', 'type', 'mentor', 'student', 'start_date', 'end_date', 'status',
              'tags', 'file')

    def get_success_url(self):
        self.object.time_edit = timezone.now()
        self.object.save()
        return reverse_lazy('interaction-detail', kwargs={'pk': self.object.id})
