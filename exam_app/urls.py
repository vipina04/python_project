from django.urls import path

from exam_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('student_register',views.student_register,name='student_register'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('exam_view/',views.exam_view,name='exam_view'),
    path('student_view/',views.student_view,name='student_view'),
    path('exam_add/',views.exam_add,name='exam_add'),
    path('student_home',views.student_home,name='student_home'),
    path('my_profile_view/<int:id>/',views.my_profile_view,name='my_profile_view'),
    path('student_exam_view',views.student_exam_view,name='student_exam_view'),
    path('exam_questions',views.attend,name='exam_questions')

]
