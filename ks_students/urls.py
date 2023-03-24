from django.urls import path
from ks_students.views import StudentsListView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentDetailView


urlpatterns = [
    path('', StudentsListView.as_view(template_name="student/students.html"), name='students-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

]
