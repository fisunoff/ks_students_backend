from django.urls import reverse_lazy
from tags.models import Tag
from djangoProject_students.edited_views import CreateViewDecorated, SingleTableViewDecorated, DetailViewDecorated
from tags.tables import TagsTable
# Create your views here.


class TagsListView(SingleTableViewDecorated):
    model = Tag
    template_name = 'tag/list.html'
    table_class = TagsTable


class TagDetailView(DetailViewDecorated):
    model = Tag
    template_name = 'tag/detail.html'
    context_object_name = 'tag'


class TagCreateView(CreateViewDecorated):
    model = Tag
    template_name = 'tag/create.html'
    fields = ('tag_name', )
    success_url = reverse_lazy('tags-list')
