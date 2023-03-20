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


@method_decorator(login_required, name='dispatch')
class InteractionCreateView(CreateView):
    model = Interaction
    template_name = 'interaction/create.html'
    fields = ('interaction_name', 'description', 'type', 'mentor', 'student', 'start_date', 'end_date', 'status', 'tags')
    success_url = reverse_lazy('interactions-list')


class InteractionDetailView(DetailView):
    model = Interaction
    template_name = 'interaction/detail.html'
    context_object_name = 'interaction'


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
    fields = ('interaction_name', 'description', 'type', 'mentor', 'student', 'start_date', 'end_date', 'status', 'tags')

    def get_success_url(self):
        self.object.time_edit = timezone.now()
        self.object.save()
        return reverse_lazy('interaction_detail', kwargs={'pk': self.object.id})
