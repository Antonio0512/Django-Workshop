from django.shortcuts import render

from petstagram.pets.models import Pet


def add_pets(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username, slug_pet):
    pet = Pet.objects.get(slug=slug_pet)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, 'pets/pet-details-page.html', context=context)


def edit_pets(request, username, slug_pet):
    return render(request, 'pets/pet-edit-page.html')


def delete_pets(request, username, slug_pet):
    return render(request, 'pets/pet-delete-page.html')
