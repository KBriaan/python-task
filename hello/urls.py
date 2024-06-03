from  . import views
from django.urls import path

urlpatterns =[
    path("", views.index, name='index'),
    path('<str:name>', views.greet, name='greet'),
    path('brian', views.brian, name='brian'),
    path('joyline', views.joyline, name='joyline'),

]