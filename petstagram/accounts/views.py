from django.shortcuts import render


def page_register(request):
    return render(request, 'accounts/register-page.html')


def page_login(request):
    return render(request, 'accounts/login-page.html')


def account_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def account_edit(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def account_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')