from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('all_task/', views.all_task, name='alltask'),
    path('create_task/', views.create_task,name='createtask'),
    path('update_task/<int:pk>', views.update_task, name='updatetask'),
    path('delete_task/<int:pk>', views.delete_task, name='deletetask'),
    path('task/<int:pk>', views.detail_task, name='detailtask'),
    path('search/', views.search_task, name='searchtask'),
    
]