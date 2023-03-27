from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from tags.models import Tag

# Create your views here.


@method_decorator(login_required, name='dispatch')
class TagsListView(ListView):
    model = Tag

    template_name = 'tag/list.html'
    context_object_name = 'tags'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TagsListView, self).get_context_data(**kwargs)
        tags = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(tags, self.paginate_by)
        try:
            tags = paginator.page(page)
        except PageNotAnInteger:
            tags = paginator.page(1)
        except EmptyPage:
            tags = paginator.page(paginator.num_pages)
        context['tags'] = tags
        return context


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
