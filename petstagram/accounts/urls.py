from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.page_register, name='page-register'),
    path('login', views.page_login, name='page-login'),
    path('profile/<int:pk>/', include([
        path('', views.account_details, name='profile-page'),
        path('edit', views.account_edit, name='profile-edit'),
        path('delete', views.account_delete, name='profile-delete'),
    ]))
]