from django.urls import path
from . import views

urlpatterns = [
    # path의 1번째 인자의 uri경로에 매칭될 경우 2번째 인자의 view파일을 실행하라
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/result/', views.results, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]

