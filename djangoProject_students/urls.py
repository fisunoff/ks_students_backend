"""djangoProject_students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ks_students.views import StudentsListView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentDetailView
from interaction.views import InteractionsListView, InteractionCreateView, InteractionDetailView, InteractionDeleteView, InteractionUpdateView
from mentor.views import MentorsListView, MentorDetailView, MentorUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentsListView.as_view(template_name="student/students.html"), name='students_list'),
    path('students/create', StudentCreateView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/update', StudentUpdateView.as_view()),
    path('students/<int:pk>/delete', StudentDeleteView.as_view(), name='student_delete'),
    path('interactions', InteractionsListView.as_view(), name="interactions-list"),
    path('interactions/create', InteractionCreateView.as_view()),
    path('interactions/<int:pk>/', InteractionDetailView.as_view(), name='interaction_detail'),
    path('interactions/<int:pk>/update', InteractionUpdateView.as_view(), name='interaction_update'),
    path('interactions/<int:pk>/delete', InteractionDeleteView.as_view(), name='interaction_delete'),

    path('mentors', MentorsListView.as_view(), name="mentors-list"),
    path('mentors/<int:pk>/', MentorDetailView.as_view(), name='mentor_detail'),
    path('mentors/<int:pk>/update', MentorUpdateView.as_view(), name='mentor_update'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('', StudentsListView.as_view(template_name="student/students.html"), name='students_list'),
]
