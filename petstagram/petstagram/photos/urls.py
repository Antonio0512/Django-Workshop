from django.urls import path, include

from petstagram.photos import views

urlpatterns = (
    path('add/', views.add_photos, name='photos-add'),
    path('<int:pk>/', include([
        path('', views.details_photos, name='photo-details'),
        path('edit/', views.edit_photos, name='photo-edit'),
    ])),
)
