from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from interaction.models import Interaction


class InteractionsListView(ListView):
    model = Interaction

    template_name = 'interaction/interactions.html'
    context_object_name = 'interactions'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(InteractionsListView, self).get_context_data(**kwargs)
        interactions = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(interactions, self.paginate_by)
        try:
            interactions = paginator.page(page)
        except PageNotAnInteger:
            interactions = paginator.page(1)
        except EmptyPage:
            interactions = paginator.page(paginator.num_pages)
        context['interactions'] = interactions
        return context

    def get_queryset(self):
        order_by = self.request.GET.get('order_by') or '-interaction_name'
        if order_by not in ['interaction_name', 'mentor', 'start_date', 'end_date', 'status']:
            order_by = 'interaction_name'
        qs = super().get_queryset()
        return qs.order_by(order_by)


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


class InteractionDetailView(DetailView):
    model = Interaction
    template_name = 'interaction/detail.html'
    context_object_name = 'interaction'

    def get_context_data(self, **kwargs):
        context = super(InteractionDetailView, self).get_context_data(**kwargs)
        context['filename'] = self.object.get_file_name()
        tags = ",".join([str(i.id) for i in self.object.tags.all()])
        context['to_copy'] = f"?interaction_name={self.object.interaction_name}&description={self.object.description}" \
                             f"&type={self.object.type.id}&mentor={self.object.mentor.id}&student={self.object.student.id}" \
                             f"&start_date={self.object.start_date}&end_date={self.object.end_date}" \
                             f"&status={self.object.status.id}&tags={tags}"
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
