from django.shortcuts import render

# Create your views here.
from djangoProject_students.edited_views import CreateViewDecorated, SingleTableViewDecorated, DetailViewDecorated,\
    DeleteViewDecorated, UpdateViewDecorated
from django.urls import reverse_lazy
from django.utils import timezone
from interaction.models import Interaction
from interaction.tables import InteractionTable


class InteractionsListView(SingleTableViewDecorated):
    model = Interaction
    template_name = 'interaction/interactions.html'
    table_class = InteractionTable


class InteractionCreateView(CreateViewDecorated):
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


class InteractionDetailView(DetailViewDecorated):
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


class InteractionDeleteView(DeleteViewDecorated):
    model = Interaction
    template_name = 'interaction/delete.html'
    success_url = reverse_lazy('interactions-list')


class InteractionUpdateView(UpdateViewDecorated):

    model = Interaction
    template_name = 'interaction/update.html'
    context_object_name = 'interaction'
    fields = ('interaction_name', 'description', 'type', 'mentor', 'student', 'start_date', 'end_date', 'status',
              'tags', 'file')

    def get_success_url(self):
        self.object.time_edit = timezone.now()
        self.object.save()
        return reverse_lazy('interaction-detail', kwargs={'pk': self.object.id})
