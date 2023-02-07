from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add/', views.add),
    path('save', views.save),
    path('update/<int:id>', views.update),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete)
]