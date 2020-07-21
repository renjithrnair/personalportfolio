from django.conf.urls import url
from .views import HomeTemplateView

urlpatterns = [
    url('', HomeTemplateView.as_view()),
]