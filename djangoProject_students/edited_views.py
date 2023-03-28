from django.views import generic
import django_tables2
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class CreateViewDecorated(generic.CreateView):
    pass


@method_decorator(login_required, name='dispatch')
class DetailViewDecorated(generic.DetailView):
    pass


@method_decorator(login_required, name='dispatch')
class DeleteViewDecorated(generic.DeleteView):
    pass


@method_decorator(login_required, name='dispatch')
class UpdateViewDecorated(generic.UpdateView):
    pass


@method_decorator(login_required, name='dispatch')
class SingleTableViewDecorated(django_tables2.SingleTableView):
    pass
