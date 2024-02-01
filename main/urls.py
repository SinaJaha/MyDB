from django.urls import  path
from . import views

# koble mine views med en url
urlpatterns = [
    path('<int:id>', views.index, name='index'),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('all/', views.showAll, name='all'),
]