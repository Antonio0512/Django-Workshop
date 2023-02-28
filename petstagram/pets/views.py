from django.shortcuts import render, redirect

from common.forms import CommentForm
from pets.models import Pet
from pets.forms import PetForm, PetDeleteForm


def pet_add(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile-page', pk=1)

    context = {
        'form': form
    }

    return render(request, 'pets/pet-add-page.html', context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(pet_slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()

    context = {
        "pet": pet,
        "all_photos": all_photos,
        "comment_form": comment_form
    }
    return render(request, 'pets/pet-details-page.html', context=context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(pet_slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)

        context = {
            'form': form,
        }
        return render(request, 'pets/pet-edit-page.html', context)

    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(pet_slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-page', pk=1)

    else:
        form = PetDeleteForm(initial=pet.__dict__)
        context = {
            'form': form
        }
        return render(request, 'pets/pet-delete-page.html', context)
