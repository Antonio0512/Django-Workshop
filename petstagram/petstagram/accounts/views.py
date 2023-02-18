from django.shortcuts import render


def register_profile(request):
    return render(request, 'accounts/register-page.html')


def login_profile(request):
    return render(request, 'accounts/login-page.html')


def show_details_profile(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')