from django.urls import path
from interaction.views import InteractionsListView, InteractionCreateView, InteractionDetailView, InteractionDeleteView, InteractionUpdateView


urlpatterns = [

    path('', InteractionsListView.as_view(), name='interactions-list'),
    path('create/', InteractionCreateView.as_view(), name='interaction-create'),
    path('<int:pk>/', InteractionDetailView.as_view(), name='interaction-detail'),
    path('<int:pk>/update/', InteractionUpdateView.as_view(), name='interaction-update'),
    path('<int:pk>/delete/', InteractionDeleteView.as_view(), name='interaction-delete'),

]
