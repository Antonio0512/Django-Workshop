from django.urls import path, include

from petstagram.pets import views

urlpatterns = (
    path('add/', views.add_pets, name='pets-add'),
    path('<str:username>/pet/<slug:slug_pet>/', include([
        path('', views.pet_details, name='pets-details'),
        path('edit/', views.edit_pets, name='pets-edit'),
        path('delete/', views.delete_pets, name='pets-delete')
    ]))
)
