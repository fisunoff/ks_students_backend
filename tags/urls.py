from django.urls import path, include
from tags.views import TagsListView, TagDetailView, TagCreateView

urlpatterns = [
    path('', TagsListView.as_view(), name='tags-list'),
    path('<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('create/', TagCreateView.as_view(), name='tag-create'),
]
