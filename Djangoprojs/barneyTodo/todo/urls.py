from django.urls import path, include
from . import views
from .views import TodoCreateView, ShoppingCreateView, MeetCreateView

# TodoDeleteView,ShoppingDeleteView, MeetDeleteView


urlpatterns = [
    path('', views.profile, name='todo-profile'),
    path('', include('users.urls')),
    path('new/todo/', TodoCreateView.as_view(), name='todo-create'),
    path('complete/<int:pk>/', views.completeTodo, name='complete'),
#    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
    path('new/shopping/', ShoppingCreateView.as_view(), name='shopping-create'),
    path('complete/<int:pk>/', views.completeShopping, name='complete'),
#    path('shopping/<int:pk>/delete/', ShoppingDeleteView.as_view(), name='shopping-delete'),
    path('new/meet/', MeetCreateView.as_view(), name='meet-create'),
    path('complete/<int:pk>/', views.completeMeet, name='complete'),
#    path('meet/<int:pk>/delete/', MeetDeleteView.as_view(), name='meet-delete'),
]
