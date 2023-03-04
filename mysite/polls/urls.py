from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:questrion_id>/results/', views.results, name='results'),
    path('<int:querstion_id>/vote/', views.vote, name='vote')
]