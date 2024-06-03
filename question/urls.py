from django.urls import path, include
from .views import QuestionsViewSet , index


urlpatterns = [
    path('index/', index.as_view()),
]
                                                                                       