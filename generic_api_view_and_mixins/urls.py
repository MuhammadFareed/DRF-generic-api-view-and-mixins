# from django.contrib import admin
# from django.urls import path
# from api.views import StudentList, StudentCreate, StudentRetrieve, StudentUpdate, StudentDestroy

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('student_api/', StudentList.as_view()),
#     # path('student_api/<int:pk>', StudentRetrieve.as_view()),
#     # path('student_api/', StudentCreate.as_view()),
#     # path('student_api/<int:pk>', StudentUpdate.as_view()),
#     path('student_api/<int:pk>', StudentDestroy.as_view()),
# ]


from django.contrib import admin
from django.urls import path
from api.views import LC_StudentAPI, RUD_StudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api/', LC_StudentAPI.as_view()),
    path('student_api/<int:pk>', RUD_StudentAPI.as_view()),
]
