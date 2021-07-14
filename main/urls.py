from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name = "index"),
    path('add_to/', views.add_to, name = "add_to"),
    path('delete_item/<int:item_id>', views.delete_item, name = "delete_item"),
]
