from django.urls import path

from .views import PersonList, PersonDetail, CourseList, CourseDetail, TaskDetail, TaskList, ResultList, ResultDetail

app_name = 'lms_api'

urlpatterns = [
    path('persons/', PersonList.as_view()),
    path('person/<int:pk>', PersonDetail.as_view()),
    path('courses/', CourseList.as_view()),
    path('course/<int:pk>', CourseDetail.as_view()),
    path('tasks/', TaskList.as_view()),
    path('task/<int:pk>', TaskDetail.as_view()),
    path('results/', ResultList.as_view()),
    path('result/<int:pk>', ResultDetail.as_view()),
]
