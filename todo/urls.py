from django.urls import path
from .views import TodoDetailView, TodoView


urlpatterns = [ 
    path("", TodoView.as_view()),
    path("<int:id>", TodoDetailView.as_view())
]