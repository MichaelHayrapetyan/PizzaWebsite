from django.urls import path
from . import views

app_name = 'pizza'

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('add/', views.add_pizza, name='add_pizza'),
    path('<int:pizza_id>/', views.pizza_detail, name='pizza_detail'),
    path('<int:pizza_id>/update/', views.update_pizza, name='update_pizza'),
    path('<int:pizza_id>/delete/', views.delete_pizza, name='delete_pizza'),
]
