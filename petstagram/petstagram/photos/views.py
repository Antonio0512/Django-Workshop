from django.shortcuts import render

from petstagram.photos.models import Photo


def add_photos(request):
    return render(request, 'photos/photo-add-page.html')


def details_photos(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'comments': comments,
        'likes': likes,
    }

    return render(request, 'photos/photo-details-page.html', context=context)


def edit_photos(request, pk):
    return render(request, 'photos/photo-edit-page.html')
