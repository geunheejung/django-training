from django.urls import path
from . import views

urlpatterns = [
    # path의 1번째 인자의 uri경로에 매칭될 경우 2번째 인자의 view파일을 실행하라
    path('', views.index, name='index'),
]

