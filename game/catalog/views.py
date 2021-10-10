from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from json import dumps
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def index(request):
    return render(
        request,
        'index.html',
        context={},
    )


def piano(request):
    return render(
        request,
        'catalog/piano/piano.html',
    )


def piano2(request):
    return render(
        request,
        'catalog/piano/piano2.html',
        context={'piano': dumps({'password': 'cd'})},
    )


def piano3(request):
    return render(
        request,
        'catalog/piano/piano3.html',
    )


def piano_secret(request):
    return render(
        request,
        'catalog/piano/piano_secret.html',
    )


def clock(request):
    return render(
        request,
        'catalog/clock.html',
    )


def box(request):
    return render(
        request,
        'catalog/box/box.html',
    )


def box_left(request):
    return render(
        request,
        'catalog/box/box_left.html',
    )


def box_right(request):
    return render(
        request,
        'catalog/box/box_right.html',
    )


def table_recipe(request):
    return render(
        request,
        'catalog/recipe/table_recipe.html',
    )


def book_recipe(request):
    return render(
        request,
        'catalog/recipe/book_recipe.html',
    )


def book_recipe2(request):
    return render(
        request,
        'catalog/recipe/book_recipe2.html',
    )


def bed_room(request):
    return render(
        request,
        'catalog/bed_room.html',
    )


def notes(request):
    return render(
        request,
        'catalog/notes/notes.html',
    )


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/catalog/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

#
# class Piano1View(generic.ListView):
#     model = Piano
