from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView
from projectapp.views import ProjectCreateView, ProjectListView, ProjectDetailView

app_name = 'projectapp'

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path("detail/<int:pk>", ProjectDetailView.as_view(template_name="projectapp/detail.html"), name="detail"),
]