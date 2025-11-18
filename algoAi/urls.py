from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reglog_details/', views.regLog_details, name='reglog_details'),
    path('reglog_atelier_C/', views.regLog_atelier_C, name='reglog_atelier_C'),
    path('reglog_tester/', views.regLog_tester, name='reglog_tester'),
    path('reglog_prediction/', views.regLog_prediction, name='regLog_prediction'),
    path('arbre_decision_details/', views.arbre_decision_details, name='arbre_decision_details'),
    path('arbre_atelier_C/', views.arbre_atelier_C, name='arbre_atelier_C'),
    path('svm_details/', views.svm_details, name='svm_details'),
    path('svm_atelier_C/', views.svm_atelier_C, name='svm_atelier_C'),
    path('svm_atelier_R/', views.svm_atelier_R, name='svm_atelier_R'),
    path('random_forest_details/', views.random_forest_details, name='random_forest_details'),
    path('random_forest_atelier_C/', views.random_forest_atelier_C, name='random_forest_atelier_C'),
    path('xgboost_details/', views.xgboost_details, name='xgboost_details'),
    path('xgboost_atelier_C/', views.xgboost_atelier_C, name='xgboost_atelier_C'),
]