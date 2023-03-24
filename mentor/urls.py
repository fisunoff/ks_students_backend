from django.urls import path
from mentor.views import MentorsListView, MentorDetailView, MentorUpdateView


urlpatterns = [
    path('', MentorsListView.as_view(), name="mentors-list"),
    path('<int:pk>/', MentorDetailView.as_view(), name='mentor-detail'),
    path('<int:pk>/update/', MentorUpdateView.as_view(), name='mentor-update'),
]
