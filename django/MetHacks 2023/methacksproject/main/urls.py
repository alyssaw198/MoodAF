from django.urls import path, include
from main import views

#Specifies all the PATHS in the website

urlpatterns = [
    path('', views.home, name='home'), #when there is no path specified, run the home function in views.py 
    path('form/', views.form, name='form'),
    path('postForm/', views.postForm, name='postForm'),
    path('summary/', views.summary, name='summary'),
    path('viewEntries/', views.viewEntries, name='viewEntries'),
    path('community/', views.analyzeAll, name='community'),
    path('filterNew/', views.filterNew, name='filterNew'),
    path('filterOld/', views.filterOld, name='filterOld')
    #path('summary', views.summary, name='summary')
    #TODO: define the different paths (different web 'pages') associated with the website
]