"""defines url patterns for learning log"""

from django.urls import path
from . import views

#request for specific url patterns in html files
app_name = 'learning_logs'
urlpatterns = [
    #home page
    path('', views.index, name='index'),
    #topic page
    path('topics/', views.topics, name='topics'),
    #a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for a new user topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #entries for each new user topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #page for editing entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

