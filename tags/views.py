from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView
from tags.models import Tag
from django_tables2 import SingleTableView
from tags.tables import TagsTable
# Create your views here.


@method_decorator(login_required, name='dispatch')
class TagsListView(SingleTableView):
    model = Tag
    template_name = 'tag/list.html'
    table_class = TagsTable


@method_decorator(login_required, name='dispatch')
class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag/detail.html'
    context_object_name = 'tag'


@method_decorator(login_required, name='dispatch')
class TagCreateView(CreateView):
    model = Tag
    template_name = 'tag/create.html'
    fields = ('tag_name', )
    success_url = reverse_lazy('tags-list')
